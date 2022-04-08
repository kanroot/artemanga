from enum import Enum


class EstadoTicket(Enum):
    PENDIENTE = 1
    RESUELTO = 2
    CANCELADO = 3


ESTADO_TICKET_CHOICES = [[estadoTicket.value, estadoTicket.name.capitalize()] for estadoTicket in EstadoTicket]
