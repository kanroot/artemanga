from enum import Enum


class TipoTicket(Enum):
    SUGERENCIA = 1
    AYUDA = 2


TIPO_TICKET_CHOICES = [[tipoTicket.value, tipoTicket.name.capitalize()] for tipoTicket in TipoTicket]
