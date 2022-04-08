from enum import Enum


class EstadoDespacho(Enum):
    """
    Enum para el estado de una venta.
    """
    PENDIENTE = 1
    EN_PROCESO = 2
    FINALIZADA = 3
    CANCELADA = 4


ESTADO_DESPACHO_CHOICES = [[estadoDespacho.value, estadoDespacho.name.capitalize()] for estadoDespacho in
                           EstadoDespacho]
