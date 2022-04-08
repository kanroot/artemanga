from enum import Enum


class EstadoDes(Enum):
    PENDIENTE = 1
    EN_PROCESO = 2
    FINALIZADO = 3
    FALLIDO = 4


ESTADO_DESPACHO_CHOICE = [[estadoDes.value, estadoDes.name.capitalize()] for estadoDes in EstadoDes]
