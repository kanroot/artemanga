from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from cuenta_usuario.restriccion import VistaRestringida
from cuenta_usuario.enums.opciones import TipoUsuario
from artemangaweb.mixins import MensajeResultadoFormMixin
from venta.models import Venta
from venta.tipo_enum.estado_venta import EstadoVenta


class VentasLisView(VistaRestringida, ListView):
    usuarios_permitidos = [TipoUsuario.VENTAS]
    model = Venta
    template_name = 'ventas/listado_ventas.html'
    queryset = Venta.objects.filter(estado=EstadoVenta.PENDIENTE.value)
    paginate_by = 10
    ordering = ['fecha_venta']
    context_object_name = 'ventas'


class VentasAprobadasLisView(VistaRestringida, ListView):
    usuarios_permitidos = [TipoUsuario.VENTAS]
    model = Venta
    template_name = 'ventas/listado_ventas.html'
    queryset = Venta.objects.filter(estado=EstadoVenta.APROBADA.value)
    paginate_by = 10
    ordering = ['fecha_venta']
    context_object_name = 'ventas'


class VentaUpdateView(VistaRestringida, MensajeResultadoFormMixin, UpdateView):
    usuarios_permitidos = [TipoUsuario.VENTAS]
    model = Venta
    template_name = 'CRUD/form_generico.html'
    success_url = reverse_lazy('ventas-validar')
    fields = ['estado']
