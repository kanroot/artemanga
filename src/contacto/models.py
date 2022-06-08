from django.db import models
from cuenta_usuario.models import Usuario
from venta.models import Venta
from .enums.estado_ticket import ESTADO_TICKET_CHOICES, EstadoTicket
from .enums.tipo_ticket import TIPO_TICKET_CHOICES, TipoTicket
from ckeditor.fields import RichTextField


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.PositiveSmallIntegerField(choices=TIPO_TICKET_CHOICES, default=TipoTicket.AYUDA.value)
    titulo = models.CharField(max_length=100, verbose_name='Breve descripción de este ticket')

    # campos automáticos
    fecha_creacion = models.DateTimeField(verbose_name="fecha de creacion", auto_now_add=True)
    fecha_modificacion = models.DateTimeField(verbose_name="fecha de modificacion", auto_now=True)
    estado = models.PositiveSmallIntegerField(choices=ESTADO_TICKET_CHOICES, default=EstadoTicket.ABIERTO.value)
    cantidad_mensajes = models.PositiveSmallIntegerField(default=0)
    # conexiones
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    @property
    def tipo_ticket_humanizado(self):
        return TipoTicket(self.tipo).name.title()

    @property
    def estado_ticket_humanizado(self):
        return EstadoTicket(self.estado).name.title()

    @property
    def mensajes(self):
        return Mensaje.objects.filter(ticket=self).order_by('fecha_creacion')

    def __str__(self):
        return f'{self.id} - {self.titulo} ({self.cantidad_mensajes} mensajes)'


class Mensaje(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(verbose_name="fecha de creacion", auto_now_add=True)
    texto = RichTextField(verbose_name='texto')
    # conexiones
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.ticket.cantidad_mensajes += 1
        self.ticket.save()
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'#{self.id} - {self.ticket.titulo}'
