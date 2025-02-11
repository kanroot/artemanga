from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from cuenta_usuario.restriccion import VistaRestringida
from cuenta_usuario.enums.opciones import TipoUsuario
from artemangaweb.mixins import MensajeResultadoFormMixin, TituloPaginaMixin
from venta.models import Venta
from venta.enums.opciones import EstadoVenta


class VentasPendientesLisView(TituloPaginaMixin, VistaRestringida, ListView):
    titulo_pagina = "Ventas Pendientes"
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    model = Venta
    template_name = 'administración/ventas/listado_ventas.html'
    queryset = Venta.objects.filter(estado=EstadoVenta.PENDIENTE.value)
    paginate_by = 10
    ordering = ['fecha_venta']
    context_object_name = 'ventas'


class VentasAprobadasLisView(TituloPaginaMixin, VistaRestringida, ListView):
    titulo_pagina = "Ventas Aprobadas"
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    model = Venta
    template_name = 'administración/ventas/listado_ventas.html'
    queryset = Venta.objects.filter(estado=EstadoVenta.APROBADA.value)
    paginate_by = 10
    ordering = ['-fecha_venta']
    context_object_name = 'ventas'


class VentaUpdateView(VistaRestringida, MensajeResultadoFormMixin, UpdateView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    model = Venta
    template_name = 'administración/CRUD/form_generico.html'
    success_url = reverse_lazy('ventas-validar')
    fields = ['estado']
