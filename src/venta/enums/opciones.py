from enum import Enum


class EstadoVenta(Enum):
    """
    Enum que representa los estados de una venta.
    """
    PENDIENTE = 1
    CANCELADA = 2
    APROBADA = 3


ESTADO_VENTA_CHOICES = [[estadoVenta.value, estadoVenta.name.capitalize()] for estadoVenta in EstadoVenta]


class EstadoDes(Enum):
    PENDIENTE = 1
    EN_PROCESO = 2
    FINALIZADO = 3
    FALLIDO = 4


ESTADO_DESPACHO_CHOICE = [[estadoDes.value, estadoDes.name.capitalize()] for estadoDes in EstadoDes]
