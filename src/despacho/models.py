from django.db import models
from .tipo_enum.estado_despacho import ESTADO_DESPACHO_CHOICE, EstadoDes
from cuenta_usuario.models import Usuario


class Despacho(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=200, verbose_name="calle")
    numero = models.CharField(max_length=200, verbose_name="numero")
    departamento = models.CharField(max_length=200, verbose_name="departamento", blank=True)
    piso = models.CharField(max_length=200, verbose_name="piso", blank=True, null=True)
    region = models.CharField(max_length=200, verbose_name="region")
    ciudad = models.CharField(max_length=200, verbose_name="ciudad")
    codigo_postal = models.CharField(max_length=200, verbose_name="codigo postal")
    telefono = models.IntegerField(verbose_name="telefono")
    estado = models.PositiveSmallIntegerField(choices=ESTADO_DESPACHO_CHOICE, default=EstadoDes.PENDIENTE.value)
    # conexiones
    # no t0d0 usuario debe teber un despacho
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.id}"

    @property
    def get_estado(self):
        return self.estado

    @property
    def get_codigo_postal(self):
        return self.codigo_postal

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
