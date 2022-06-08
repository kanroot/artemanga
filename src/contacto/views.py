from django.shortcuts import redirect, reverse, render
from django.views.generic import DetailView, View, TemplateView
from django.views.generic.edit import FormMixin

from artemangaweb.mixins import VistaRestringidaMixin
from cuenta_usuario.enums.opciones import TipoUsuario
from inventario.vistas_modelos.vistas_genericas import ListaGenericaView
from .enums.estado_ticket import EstadoTicket
from .models import Ticket, Mensaje
from .forms import CrearMensajeForm, CrearTicketForm
from django.http import Http404


# mixin especial que restringe la vista al dueño del ticket o los administradores
class DuennoOAdminsRestringidoMixin:
    ticket = None
    def es_admin(self, usuario):
        return usuario.tipo_usuario == TipoUsuario.ADMINISTRADOR.value or usuario == TipoUsuario.BODEGA.value or usuario == TipoUsuario.VENTAS.value

    def dispatch(self, request, *args, **kwargs):
        self.get_ticket()
        if self.ticket.usuario != request.user and not self.es_admin(request.user):
            raise Http404()
        return super().dispatch(request, *args, **kwargs)

    def get_ticket(self):
        if self.ticket is None:
            self.ticket = Ticket.objects.get(pk=self.kwargs['pk'])



class TicketDetalle(DuennoOAdminsRestringidoMixin, FormMixin, DetailView):
    template_name = 'web/contacto/detalle.html'
    queryset = Ticket.objects.all()
    form_class = CrearMensajeForm

    def get_success_url(self):
        return reverse('contacto-detalle', kwargs={'pk': self.object.pk})


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        nuevo_mensaje = Mensaje(
            ticket=self.object,
            usuario=self.request.user,
            texto=form.cleaned_data['texto']
        )
        nuevo_mensaje.save()
        return super().form_valid(form)


class CerrarTicket(DuennoOAdminsRestringidoMixin, View):
    def get(self, request, *args, **kwargs):
        ticket = Ticket.objects.get(pk=kwargs['pk'])
        ticket.estado = EstadoTicket.CERRADO.value
        ticket.save()
        return redirect('contacto-detalle', pk=kwargs['pk'])


class ReabrirTicket(DuennoOAdminsRestringidoMixin, View):
    def get(self, request, *args, **kwargs):
        ticket = Ticket.objects.get(pk=kwargs['pk'])
        ticket.estado = EstadoTicket.ABIERTO.value
        ticket.save()
        return redirect('contacto-detalle', pk=kwargs['pk'])


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
    tabla_boton_editar = 'contacto-detalle'
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
    ordering = ['-estado']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tickets'] = Ticket.objects.filter(usuario=self.request.user).order_by('estado')
        return context


class CrearTicketView(VistaRestringidaMixin, TemplateView):
    usuarios_permitidos = VistaRestringidaMixin.todos_los_usuarios
    template_name = 'web/contacto/crear_ticket.html'


    def get(self, request, *args, **kwargs):
        ticket_form = CrearTicketForm(usuario=request.user)
        mensaje_form = CrearMensajeForm()
        return render(request, self.template_name, {'ticket_form': ticket_form, 'mensaje_form': mensaje_form})

    def post(self, request, *args, **kwargs):
        ticket_form = CrearTicketForm(request.POST, usuario=request.user)
        mensaje_form = CrearMensajeForm(request.POST)

        if ticket_form.is_valid() and mensaje_form.is_valid():
            ticket = Ticket(
                usuario=request.user,
                tipo=ticket_form.cleaned_data['tipo'],
                titulo=ticket_form.cleaned_data['titulo'],
                venta=ticket_form.cleaned_data['venta'],
            )
            ticket.save()
            Mensaje(
                ticket=ticket,
                usuario=request.user,
                texto=mensaje_form.cleaned_data['texto']
            ).save()

            return redirect('contacto-detalle', pk=ticket.pk)
