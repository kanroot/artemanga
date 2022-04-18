from django.db import models
from despacho.models import Despacho
from inventario.models import Producto
from .tipo_enum.estado_venta import ESTADO_VENTA_CHOICES, EstadoVenta


class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="total")
    fecha_venta = models.DateField(verbose_name="fecha venta", auto_now_add=True)
    estado = models.PositiveSmallIntegerField(choices=ESTADO_VENTA_CHOICES, default=EstadoVenta.PENDIENTE.value)
    # conexiones
    despacho = models.OneToOneField(Despacho, on_delete=models.CASCADE)


class VentaProducto(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f""

    class Meta:
        verbose_name = "Productos de la venta"
        verbose_name_plural = "Productos de la venta"