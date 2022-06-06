from enum import Enum


class EstadoTicket(Enum):
    ABIERTO = 1
    CERRADO = 2


ESTADO_TICKET_CHOICES = [[estadoTicket.value, estadoTicket.name.capitalize()] for estadoTicket in EstadoTicket]
