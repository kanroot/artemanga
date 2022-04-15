from django.db import models
from .tipo_enum.estado_despacho import ESTADO_DESPACHO_CHOICE, EstadoDes
from cuenta_usuario.models import Usuario


class Region(models.Model):
    region = models.CharField(primary_key=True, max_length=100, choices=REGION_CHILE_CHOISE)


class Cuidad(models.Model):
    nombre = models.CharField(primary_key=True, max_length=100, choices=CIUDAD_CHILE_CHOICE)
    # conexiones
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class Despacho(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=200, verbose_name="calle")
    numero = models.CharField(max_length=200, verbose_name="numero")
    departamento = models.CharField(max_length=200, verbose_name="departamento", blank=True)
    piso = models.CharField(max_length=200, verbose_name="piso", blank=True, null=True)
    ciudad = models.CharField(max_length=200, verbose_name="ciudad")
    codigo_postal = models.CharField(max_length=200, verbose_name="codigo postal")
    telefono = models.IntegerField(verbose_name="telefono")
    estado = models.PositiveSmallIntegerField(choices=ESTADO_DESPACHO_CHOICE, default=EstadoDes.PENDIENTE.value)
    # conexiones
    # no t0d0 usuario debe teber un despacho
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="region", blank=True, null=True)

    def __str__(self):
        return f"{self.id}"

    @property
    def direccion_completa(self):
        return f"{self.calle} " \
               f"{self.numero}" \
               f" {self.departamento} " \
               f"{self.piso} {self.region}" \
               f" {self.ciudad} " \
               f"{self.codigo_postal}"

    @property
    def direccion_corta(self):
        return f"{self.calle} {self.numero}"
