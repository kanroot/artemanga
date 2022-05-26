from django.views.generic import TemplateView
from artemangaweb.mixins import VistaRestringidaMixin
from cuenta_usuario.enums.opciones import TipoUsuario
from django.shortcuts import redirect
from inventario.vistas_modelos.vistas_genericas import ListaGenericaView
from venta.models import Venta, Despacho
from venta.enums.opciones import EstadoVenta
from inventario.models import Producto
from cuenta_usuario.models import Usuario


class DashboardView(VistaRestringidaMixin, TemplateView):
    template_name = "administración/dashboard.html"
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA, TipoUsuario.VENTAS]
    model = Usuario

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuarios_activos'] = Usuario.objects.filter(es_activo=True)
        context['usuarios_inactivos'] = Usuario.objects.filter(es_activo=False)
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.es_ventas():
            return redirect('dashboard-ventas')
        if request.user.es_bodega():
            return redirect('dashboard-bodega')
        return super().dispatch(request, *args, **kwargs)


class BodegaDashboardView(VistaRestringidaMixin, ListaGenericaView):
    template_name = "administración/bodega/tareas_urgentes.html"
    usuarios_permitidos = [TipoUsuario.BODEGA, TipoUsuario.ADMINISTRADOR]
    model = Producto
    context_object_name = 'productos'
    tabla_boton_crear = None
    tabla_boton_eliminar = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sin_stock'] = Producto.objects.filter(stock=0)
        context['bajo_stock'] = Producto.objects.filter(stock__lte=5).order_by('stock')[:10]
        context['sin_portada'] = Producto.objects.filter(portada=None) | \
                                 Producto.objects.filter(portada='portadas/portada.jpg')
        context['sin_genero'] = Producto.objects.filter(genero=None)
        context['sin_portada_o_genero'] = Producto.objects.filter(portada=None)[:10] | \
                                          Producto.objects.filter(portada='portadas/portada.jpg')[:10] | \
                                          Producto.objects.filter(genero=None)[:10]
        return context


class VentaDashboardView(ListaGenericaView):
    usuarios_permitidos = [TipoUsuario.VENTAS, TipoUsuario.ADMINISTRADOR]
    template_name = 'administración/ventas/tareas_urgentes.html'
    model = Venta
    tabla_boton_crear = None
    tabla_boton_eliminar = None
    tabla_boton_editar = 'venta-validar-producto'
    tabla_boton_editar_producto = 'ventas-actualizar-producto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ventas_pendientes'] = Venta.objects.filter(estado=EstadoVenta.PENDIENTE.value)
        context['despachos_sin_seguimiento'] = Despacho.objects.filter(codigo_seguimiento=None)
        context['ventas_cancelada'] = Venta.objects.filter(estado=EstadoVenta.CANCELADA.value)
        context['ventas_aprobada'] = Venta.objects.filter(estado=EstadoVenta.APROBADA.value)
        context['productos_destacados'] = Producto.objects.filter(es_destacado=True)
        context['productos_nuevos'] = Producto.objects.filter(es_nuevo=True)
        context['ultimas_ventas_sin_aprobar'] = Venta.objects.filter(estado=EstadoVenta.PENDIENTE.value).order_by(
            '-fecha_venta')[:6]
        context['productos_sin_publicar'] = Producto.objects.filter(esta_publicado=False)[:6]
        context['ventas_aprobadas_sin_boleta'] = Venta.objects.filter(estado=EstadoVenta.APROBADA.value, boleta='')[:6]
        return context
