from django.db import models
from cuenta_usuario.models import Usuario
from venta.models import Venta
from .enums.estado_ticket import ESTADO_TICKET_CHOICES, EstadoTicket
from .enums.tipo_ticket import TIPO_TICKET_CHOICES, TipoTicket
from ckeditor.fields import RichTextField
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from .signals import nuevo_ticket_signal, nuevo_mensaje_admin_signal, nuevo_mensaje_cliente_signal, estado_ticket_cambiado_signal
from cuenta_usuario.enums.opciones import TipoUsuario

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
    def tipo_humanizado(self):
        return TipoTicket(self.tipo).name.title()

    @property
    def estado_humanizado(self):
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


@receiver(post_save, sender=Ticket)
def ticket_post_save(sender, instance: Ticket, **kwargs):
    if instance.cantidad_mensajes == 0:
        # se asume que es un ticket nuevo
        nuevo_ticket_signal.send(sender=Ticket.__class__, instance=instance)
    else:
        # modificando ticket existente
        pass


@receiver(pre_save, sender=Ticket)
def ticket_pre_save(sender, instance: Ticket, **kwargs):
    try:
        obj = Ticket.objects.get(id=instance.id)
    except Ticket.DoesNotExist:
        # es un nuevo ticket, no existía antes
        pass
    else:
        # modificando ticket existente, comprobemos si cambió el estado
        if obj.estado != instance.estado:
            estado_ticket_cambiado_signal.send(sender=Ticket.__class__, instance=instance)


@receiver(pre_save, sender=Mensaje)
def mensaje_pre_save(sender, instance: Mensaje, **kwargs):
    # los mensajes no se pueden editar, por lo tanto, asumimos creación.
    if instance.usuario.tipo_usuario == TipoUsuario.ADMINISTRADOR.value \
            or instance.usuario.tipo_usuario == TipoUsuario.VENTAS.value\
            or instance.usuario.tipo_usuario == TipoUsuario.BODEGA.value:
        # el mensaje es una respuesta de administrador, notificar al cliente
        nuevo_mensaje_cliente_signal.send(sender=Mensaje.__class__, instance=instance)

    elif instance.usuario.tipo_usuario == TipoUsuario.CLIENTE.value:
        if instance.ticket.cantidad_mensajes == 0:
            # este mensaje es el primer mensaje del ticket, omitir notificación
            return
        # el mensaje es una respuesta de cliente, notificar a los administradores
        nuevo_mensaje_admin_signal.send(sender=Mensaje.__class__, instance=instance)