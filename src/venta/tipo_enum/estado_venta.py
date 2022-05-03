from enum import Enum


class EstadoVenta(Enum):
    """
    Enum que representa los estados de una venta.
    """
    PENDIENTE = 1
    CANCELADA = 2
    APROBADA = 3


ESTADO_VENTA_CHOICES = [[estadoVenta.value, estadoVenta.name.capitalize()] for estadoVenta in EstadoVenta]
