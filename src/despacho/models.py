from django.db import models
from tipo_enum.estado_despacho import ESTADO_DESPACHO_CHOICES, estadoDespacho
from cuentausuario.models import Usuario


class Despacho(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=200, verbose_name="calle", blank=False)
    numero = models.CharField(max_length=200, verbose_name="numero", blank=False)
    departamento = models.CharField(max_length=200, verbose_name="departamento", blank=True)
    piso = models.CharField(max_length=200, verbose_name="piso", blank=True, null=True)
    region = models.CharField(max_length=200, verbose_name="region", blank=False)
    cuidad = models.CharField(max_length=200, verbose_name="cuidad", blank=False)
    codigo_postal = models.CharField(max_length=200, verbose_name="codigo postal", blank=False)
    telefono = models.IntegerField(verbose_name="telefono", blank=False)
    estado = models.PositiveSmallIntegerField(choices=ESTADO_DESPACHO_CHOICES, default=estadoDespacho.PREPARANDO.value)
    # conexiones
    # no t0d0 usuario debe teber un despacho
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.id}"

    def get_estado(self):
        return self.estado

    def direccion_completa(self):
        return f"{self.calle} " \
               f"{self.numero}" \
               f" {self.departamento} " \
               f"{self.piso} {self.region}" \
               f" {self.cuidad} " \
               f"{self.codigo_postal}"
