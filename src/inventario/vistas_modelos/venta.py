from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from artemangaweb.mixins import VistaRestringidaMixin
from cuenta_usuario.enums.opciones import TipoUsuario
from venta.enums.opciones import EstadoVenta
from venta.models import Venta, Despacho
from .vistas_genericas import ActualizarGenericoView, ListaGenericaView
from inventario.forms import DespachoForm, ActualizarVentaForm


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
    template_name = 'administración/CRUD/validar_venta.html'
    success_url = reverse_lazy('ventas-validar')
    form_class = ActualizarVentaForm
    second_form_class = DespachoForm
    fields = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        venta = get_object_or_404(Venta, pk=self.kwargs['pk'])
        context['venta'] = venta
        context['form'] = self.form_class(instance=venta)
        context['form2'] = self.second_form_class(instance=venta.despacho)
        context['titulo_pagina_dos'] = get_object_or_404(Despacho, venta__pk=self.kwargs['pk']).direccion
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        venta = get_object_or_404(Venta, pk=pk)
        venta_form = ActualizarVentaForm(instance=venta, data=request.POST, files=request.FILES or None)
        despacho = get_object_or_404(Despacho, venta__pk=pk)
        despacho_form = DespachoForm(instance=despacho, data=request.POST)

        if 'submit_venta' in request.POST:
            if venta_form.is_bound and venta_form.is_valid():
                venta_form.save()
        elif 'submit_despacho' in request.POST:
            if despacho_form.is_bound and despacho_form.is_valid():
                despacho_form.save()
        return HttpResponseRedirect(reverse('dashboard-ventas'))
