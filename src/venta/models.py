from datetime import datetime

from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from cuenta_usuario.models import Usuario
from inventario.models import Producto
from .enums.opciones import ESTADO_VENTA_CHOICES, EstadoVenta, EstadoDes, ESTADO_DESPACHO_CHOICE
from .signals import venta_actualizada_signal, despacho_actualizado_signal


class Region(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    # conexion con la tabla region
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='provincias')

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    # conexion con la tabla provincia
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='comunas')

    def __str__(self):
        return self.nombre


class Direccion(models.Model):
    class Meta:
        verbose_name_plural = 'Direcciones'

    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    departamento = models.CharField(max_length=200, verbose_name="departamento", blank=True)
    piso = models.CharField(max_length=200, verbose_name="piso", blank=True, null=True)
    codigo_postal = models.IntegerField(verbose_name="codigo postal", validators=[
        RegexValidator(
            regex=r'^[0-9]{7}$',
            message='El codigo postal debe tener 7 digitos. Ej: 1234567',
            code='invalid_codigo_postal'
        )
    ])
    telefono = models.CharField(verbose_name="telefono", max_length=12, validators=[
        RegexValidator(
            regex=r'^(\+?56)?(\s?)(0?9)(\s?)[9876543]\d{7}$',
            message='El celular debe seguir el siguiente formato: +569123456789',
            code='invalid_celular')
    ])
    # conexiones
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name='direcciones')
    # un usuario puede tener más de una dirección
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='direcciones')

    @property
    def provincia(self):
        return self.comuna.provincia

    @property
    def region(self):
        return self.provincia.region

    @property
    def direccion_completa(self):
        return f"{self.calle} " \
               f"#{self.numero} " \
               f"{('depto.' + self.departamento) if self.departamento else ''} " \
               f"{('piso' + self.piso) if self.piso else ''} " \
               f"{self.comuna}, {self.provincia}, {self.region}"

    @property
    def direccion_corta(self):
        return f"{self.calle} #{self.numero}, {self.comuna}"

    def __str__(self):
        return self.direccion_completa


class Despacho(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_seguimiento = models.CharField(max_length=100, verbose_name="codigo de seguimiento Starken", blank=True)
    estado = models.PositiveSmallIntegerField(choices=ESTADO_DESPACHO_CHOICE, default=EstadoDes.PENDIENTE.value)
    # conexiones
    # una direccion puede pertenecer a un despacho o más de uno, pero un despacho puede solo pertenecer una direccion
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, verbose_name="dirección")

    @property
    def usuario(self):
        return self.direccion.usuario

    @property
    def estado_despacho(self):
        return EstadoDes(self.estado).name

    def __str__(self):
        return f"Despacho {self.id}, de {self.usuario}, en {self.direccion}"


class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.IntegerField(verbose_name="total")
    fecha_venta = models.DateField(verbose_name="fecha venta", null=True)
    estado = models.PositiveSmallIntegerField(choices=ESTADO_VENTA_CHOICES, default=EstadoVenta.PENDIENTE.value)
    imagen_deposito = models.ImageField(default='comprobantes/holder.jpg', upload_to='comprobantes/')
    boleta = models.FileField(upload_to='boletas/', null=True, blank=True)
    # conexiones
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    despacho = models.OneToOneField(Despacho, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.fecha_venta is None:
            self.fecha_venta = datetime.now()
        super().save(force_insert, force_update, using, update_fields)

    @property
    def estado_venta(self):
        return EstadoVenta(self.estado).name

    @property
    def total_humanizado(self):
        return '{:,}'.format(int(self.total)).replace(',', '.')

    @property
    def estado_boleta(self) -> bool:
        if self.boleta:
            return True
        return False

    @property
    def detalles(self):
        return VentaProducto.objects.filter(venta=self)

    def __str__(self):
        return f'Compra de {self.despacho.usuario} por ${self.total_humanizado} el {self.fecha_venta}'


class VentaProducto(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f""

    class Meta:
        verbose_name = "Productos de la venta"
        verbose_name_plural = "Productos de la venta"


class ComprobanteTemporal(models.Model):
    comprobante = models.ImageField(upload_to='tmp/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


@receiver(pre_save, sender=Venta)
def venta_pre_save(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        # estamos creando una nueva venta, no es posible obtener datos como pk o productos
        pass
    else:
        # estamos actualizando una venta, comprobemos que haya cambiado el estado
        if obj.estado != instance.estado or obj.boleta != instance.boleta:
            venta_actualizada_signal.send(sender=instance.__class__, instance=instance)


@receiver(pre_save, sender=Despacho)
def despacho_pre_save(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        # estamos creando un nuevo despacho
        pass
    else:
        # estamos actualizando un despacho, comprobemos que haya cambiado el estado o se haya adjuntado número de seguimiento
        if obj.codigo_seguimiento != instance.codigo_seguimiento:
            despacho_actualizado_signal.send(sender=instance.__class__, instance=instance)
            return
        if obj.estado != instance.estado:
            despacho_actualizado_signal.send(sender=instance.__class__, instance=instance)
