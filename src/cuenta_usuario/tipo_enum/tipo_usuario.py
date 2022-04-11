from enum import Enum


class Tipo(Enum):
    ADMINISTRADOR = 1
    VENTAS = 2
    BODEGA = 3
    CLIENTE = 4


TIPO_CHOICES = [[tipo.value, tipo.name.capitalize()] for tipo in Tipo]
