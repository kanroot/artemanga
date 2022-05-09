from django.urls import reverse_lazy

from artemangaweb.mixins import VistaRestringidaMixin
from cuenta_usuario.enums.opciones import TipoUsuario
from inventario.forms import ProductoBodegaForm, ActualizarProductoVentasForm
from inventario.models import Producto
from .vistas_genericas import CrearGenericoView, ActualizarGenericoView, EliminarGenericoView, ListaGenericaView


class ProductoListView(VistaRestringidaMixin, ListaGenericaView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Producto
    template_name = 'administración/CRUD/listado_producto.html'
    paginate_by = 10
    ordering = ['pk']
    context_object_name = 'productos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contexto_extra = {
            'url_crear': 'crear-producto',
            'url_editar': 'editar-producto',
            'url_eliminar': 'eliminar-producto',
        }

        context.update(contexto_extra)
        return context


class ProductoUpdateView(VistaRestringidaMixin, ActualizarGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Producto
    fields = None
    form_class = ProductoBodegaForm
    success_url = reverse_lazy('listado-producto')


class ProductoCreateView(VistaRestringidaMixin, CrearGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Producto
    fields = None
    form_class = ProductoBodegaForm
    success_url = reverse_lazy('listado-producto')


class ProductoDeleteView(VistaRestringidaMixin, EliminarGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Producto
    success_url = reverse_lazy('listado-producto')


class ActualizarProductoVentasView(VistaRestringidaMixin, ActualizarGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    template_name = 'administración/CRUD/form_generico.html'
    model = Producto
    fields = None
    form_class = ActualizarProductoVentasForm
    success_url = reverse_lazy('ventas-listado-productos')


class VentasListadoProductosView(VistaRestringidaMixin, ListaGenericaView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    model = Producto
    template_name = "administración/ventas/listado_productos.html"
    queryset = Producto.objects.all()
    ordering = ['esta_publicado']
    paginate_by = 10
    context_object_name = 'productos'
