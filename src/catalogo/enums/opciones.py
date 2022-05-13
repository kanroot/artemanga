from enum import Enum

class EstadoCampanna(Enum):
    DRAFT = 1
    PUBLICADA = 2
    INACTIVA = 3

ESTADO_CAMPANNA_CHOICES = [[opcion.value, opcion.name] for opcion in EstadoCampanna]

class RedirigeA(Enum):
    """
    Enum que representa a qué tipo de objetos puede una campaña de catálogo redirigir
    """
    PRODUCTO = 1
    GENERO = 2
    EDITORIAL = 3
    AUTOR = 4
    OTRO = 5

REDIRIGEA_CHOICES = [[opcion.value, opcion.name] for opcion in RedirigeA]
