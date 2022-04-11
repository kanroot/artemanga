from django.db import models


class Oferta(models.Model):
    id = models.AutoField(primary_key=True)
    descuento = models.IntegerField(verbose_name="descuento", default=10)
    fecha_inicio = models.DateField(verbose_name="fecha inicio")
    fecha_fin = models.DateField(verbose_name="fecha fin")

    def oferta_valida(self, fecha_actual):
        if self.fecha_inicio <= fecha_actual <= self.fecha_fin:
            return True
