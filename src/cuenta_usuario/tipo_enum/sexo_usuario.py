from enum import Enum


class Sexo(Enum):
    MASCULINO = 1
    FEMENINO = 2
    OTRO = 3
    NO_RESPONDE = 4


SEXO_CHOICES = [[sexo.value, sexo.name.capitalize()] for sexo in Sexo]
