from django.views.generic import TemplateView
from artemangaweb.mixins import VistaRestringidaMixin
from cuenta_usuario.enums.opciones import TipoUsuario
from django.shortcuts import redirect

from inventario.vistas_modelos.vistas_genericas import ListaGenericaView
from venta.models import Venta
from venta.enums.opciones import EstadoVenta
from inventario.models import Producto


class DashboardView(VistaRestringidaMixin, TemplateView):
    template_name = "administración/dashboard.html"
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA, TipoUsuario.VENTAS]

    def dispatch(self, request, *args, **kwargs):
        if request.user.es_ventas():
            return redirect('dashboard-ventas')
        return super().dispatch(request, *args, **kwargs)


class VentaDashboardView(ListaGenericaView):
    usuarios_permitidos = VistaRestringidaMixin.todos_los_usuarios
    template_name = 'administración/ventas/tareas_urgentes.html'
    model = Venta
    tabla_boton_crear = None
    tabla_boton_eliminar = None
    tabla_boton_editar = 'venta-validar-producto'
    tabla_boton_editar_producto = 'ventas-actualizar-producto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ventas_pendientes'] = Venta.objects.filter(estado=EstadoVenta.PENDIENTE.value)
        context['ventas_cancelada'] = Venta.objects.filter(estado=EstadoVenta.CANCELADA.value)
        context['ventas_aprobada'] = Venta.objects.filter(estado=EstadoVenta.APROBADA.value)
        context['productos_destacados'] = Producto.objects.filter(es_destacado=True)
        context['productos_nuevos'] = Producto.objects.filter(es_nuevo=True)
        context['ultimas_ventas_sin_aprobar'] = Venta.objects.filter(estado=EstadoVenta.PENDIENTE.value).order_by(
            '-fecha_venta')[:5]
        context['productos_sin_publicar'] = Producto.objects.filter(esta_publicado=False)[:]
        return context
