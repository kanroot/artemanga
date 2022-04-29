from enum import Enum


class TipoUsuario(Enum):
    ADMINISTRADOR = 1
    VENTAS = 2
    BODEGA = 3
    CLIENTE = 4


TIPO_CHOICES = [[tipo.value, tipo.name.capitalize()] for tipo in TipoUsuario]


class SexoUsuario(Enum):
    MASCULINO = 1
    FEMENINO = 2
    OTRO = 3
    NO_RESPONDE = 4


SEXO_CHOICES = [[sexo.value, sexo.name.capitalize()] for sexo in SexoUsuario]
