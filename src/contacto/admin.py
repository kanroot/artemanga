from django.contrib import admin

from .models import Ticket, Mensaje


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'tipo',
        'fecha_creacion',
        'fecha_modificacion',
        'estado',
        'venta',
        'usuario',
    )
    list_filter = (
        'fecha_creacion',
        'fecha_modificacion',
        'usuario',
    )


@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_creacion', 'texto', 'ticket', 'usuario')
    list_filter = ('fecha_creacion', 'ticket', 'usuario')
