from django.urls import reverse_lazy

from artemangaweb.mixins import VistaRestringidaMixin
from cuenta_usuario.enums.opciones import TipoUsuario
from venta.enums.opciones import EstadoVenta
from venta.models import Venta
from .vistas_genericas import ActualizarGenericoView, ListaGenericaView


class VentasPendientesLisView(VistaRestringidaMixin, ListaGenericaView):
    titulo_pagina = "Ventas Pendientes"
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    model = Venta
    template_name = 'administración/ventas/tabla_ventas.html'
    queryset = Venta.objects.filter(estado=EstadoVenta.PENDIENTE.value)
    ordering = ['fecha_venta']
    context_object_name = 'ventas'
    tabla_cabecera = ['ID', 'Total', 'Fecha de la venta', 'Imagen del depósito']
    tabla_boton_crear = None
    tabla_boton_editar = 'venta-validar-producto'
    tabla_boton_eliminar = None


class VentasAprobadasLisView(VistaRestringidaMixin, ListaGenericaView):
    titulo_pagina = "Ventas Aprobadas"
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    model = Venta
    template_name = 'administración/ventas/tabla_ventas.html'
    queryset = Venta.objects.filter(estado=EstadoVenta.APROBADA.value)
    ordering = ['-fecha_venta']
    context_object_name = 'ventas'
    tabla_cabecera = ['ID', 'Total', 'Fecha de la venta', 'Imagen del depósito']
    tabla_boton_crear = None
    tabla_boton_editar = 'venta-validar-producto'
    tabla_boton_eliminar = None


class VentaUpdateView(VistaRestringidaMixin, ActualizarGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    model = Venta
    template_name = 'administración/CRUD/form_generico.html'
    success_url = reverse_lazy('ventas-validar')
    fields = ['estado', 'boleta']
