from django.db import models


class Oferta(models.Model):
    id = models.AutoField(primary_key=True)
    descuento = models.IntegerField(verbose_name="descuento", blank=False, default=10)
    fecha_inicio = models.DateField(verbose_name="fecha inicio", blank=False, null=False)
    fecha_fin = models.DateField(verbose_name="fecha fin", blank=False, null=False)
    es_activa = models.BooleanField(default=True)
