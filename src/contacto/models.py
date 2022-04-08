from django.db import models
from cuentausuario.models import Usuario
from .tipo_enum.estado_ticket import ESTADO_TICKET_CHOICES, EstadoTicket
from .tipo_enum.tipo_ticket import TIPO_TICKET_CHOICES, TipoTicket


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.PositiveSmallIntegerField(choices=TIPO_TICKET_CHOICES, default=TipoTicket.SUGERENCIA)
    fecha_creacion = models.DateTimeField(verbose_name="fecha de creacion", blank=False, null=False)
    fecha_modificacion = models.DateTimeField(verbose_name="fecha de modificacion", blank=False, null=False)
    estado = models.PositiveSmallIntegerField(choices=ESTADO_TICKET_CHOICES, default=EstadoTicket.PENDIENTE.value)
    # conexiones
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)


class Mensaje(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(verbose_name="fecha de creacion", blank=False, null=False)
    mensaje = models.CharField(max_length=200, verbose_name="mensaje", blank=False)
    # conexiones
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Respuesta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(verbose_name="fecha de creacion", blank=False, null=False)
    respuesta = models.CharField(max_length=200, verbose_name="respuesta", blank=False)
    # conexiones
    mensaje = models.OneToOneField(Mensaje, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
