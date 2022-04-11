from django.db import models
from inventario.models import Producto


class Oferta(models.Model):
    id = models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
    descuento = models.IntegerField(verbose_name="descuento", default=10)
    fecha_inicio = models.DateField(verbose_name="fecha inicio")
    fecha_fin = models.DateField(verbose_name="fecha fin")

    def oferta_valida(self, fecha_actual):
        return (self.fecha_inicio <= fecha_actual) and (fecha_actual <= self.fecha_fin)
