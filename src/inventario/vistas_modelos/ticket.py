from artemangaweb.mixins import VistaRestringidaMixin
from contacto.enums.estado_ticket import EstadoTicket
from contacto.models import Ticket
from cuenta_usuario.enums.opciones import TipoUsuario
from inventario.vistas_modelos.vistas_genericas import ListaGenericaView


class TicketsAbiertosLisView(VistaRestringidaMixin, ListaGenericaView):
    titulo_pagina = "Tickets Abiertos"
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    model = Ticket
    template_name = 'administración/CRUD/tabla_ticket.html'
    queryset = Ticket.objects.filter(estado=EstadoTicket.ABIERTO.value)
    ordering = ['fecha_creacion']
    context_object_name = 'tickets'
    tabla_cabecera = ['Tipo', 'Fecha de creación', 'Usuario', 'Venta']
    tabla_boton_crear = None
    tabla_boton_editar = None
    tabla_boton_eliminar = None


class TicketsCerradosLisView(VistaRestringidaMixin, ListaGenericaView):
    titulo_pagina = "Tickets Cerrados"
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    model = Ticket
    template_name = 'administración/CRUD/tabla_ticket.html'
    queryset = Ticket.objects.filter(estado=EstadoTicket.CERRADO.value)
    ordering = ['fecha_creacion']
    context_object_name = 'tickets'
    tabla_cabecera = ['Tipo', 'Fecha de creación', 'Usuario', 'Venta']
    tabla_boton_crear = None
    tabla_boton_editar = None
    tabla_boton_eliminar = None


class MisTicketsView(VistaRestringidaMixin, ListaGenericaView):
    usuarios_permitidos = VistaRestringidaMixin.todos_los_usuarios
    model = Ticket
    template_name = 'web/usuario/mi_soporte.html'
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tickets'] = Ticket.objects.filter(usuario=self.request.user)
        return context


