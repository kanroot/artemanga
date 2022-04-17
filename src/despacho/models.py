from django.core.validators import RegexValidator
from django.db import models
from cuenta_usuario.models import Usuario
from .tipo_enum.estado_despacho import ESTADO_DESPACHO_CHOICE, EstadoDes
from .tipo_enum.region_chile import RegionChile


class Region(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)


class Provincia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    # conexion con la tabla region
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='provincias')


class Comuna(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    # conexion con la tabla provincia
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='comunas')


class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    departamento = models.CharField(max_length=200, verbose_name="departamento", blank=True)
    piso = models.CharField(max_length=200, verbose_name="piso", blank=True, null=True)
    codigo_postal = models.CharField(max_length=200, verbose_name="codigo postal")
    telefono = models.CharField(verbose_name="telefono", max_length=12, default='+569123456789', validators=[
        RegexValidator(
            regex=r'^(\+?56)?(\s?)(0?9)(\s?)[9876543]\d{7}$',
            message='El celular debe seguir el siguiente formato: +569123456789',
            code='invalid_celular')
    ])
    # conexiones
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name='direcciones')
    # un usuario puede tener más de una direccion, pero una direccion puede o no pertenecer a un usuario
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='direcciones', blank=True, null=True)

    @property
    def direccion_completa(self):
        return f"{self.calle} " \
               f"{self.numero}" \
               f"{self.departamento} " \
               f"{self.piso} {self.region}" \
               f"{self.codigo_postal}"

    @property
    def direccion_corta(self):
        return f"{self.calle} {self.numero}"


class Despacho(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.PositiveSmallIntegerField(choices=ESTADO_DESPACHO_CHOICE, default=EstadoDes.PENDIENTE.value)
    # conexiones
    # no t0d0 usuario debe teber un despacho
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    # una direccion puede pertenecer a un despacho o más de uno, pero un despacho puede solo pertenecer una direccion
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, verbose_name="direccion")

    def __str__(self):
        return f"{self.id}"

    @property
    def estado_usuario(self):
        return f"{self.estado}" \
               f"{self.usuario}"
