from enum import Enum

class EstadoDespacho(Enum):
    PREPARANDO = 1
    EN_DESPACHO = 2
    ENTREGADO = 3
    FALLIDO = 4


ESTADO_DESPACHO_CHOICES = [[estadoDespacho.value, estadoDespacho.name.capitalize()] for estadoDespacho in EstadoDespacho]
