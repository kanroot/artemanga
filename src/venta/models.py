from django.db import models
from despacho.models import Despacho
from inventario.models import Producto
from .tipo_enum.estado_venta import ESTADO_VENTA_CHOICES, EstadoVenta


class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="total")
    fecha_venta = models.DateField(verbose_name="fecha venta")
    estado = models.PositiveSmallIntegerField(choices=ESTADO_VENTA_CHOICES, default=EstadoVenta.PENDIENTE.value)
    productos = models.ManyToManyField(Producto)
    # conexiones
    despacho = models.OneToOneField(Despacho, on_delete=models.CASCADE)
