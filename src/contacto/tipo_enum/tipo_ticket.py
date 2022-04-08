from enum import Enum


class TipoTicket(Enum):
    DUDA = 1
    SUGERENCIA = 2
    QUEJA = 3


TIPO_TICKET_CHOICES = [[tipoTicket.value, tipoTicket.name.capitalize()] for tipoTicket in TipoTicket]
