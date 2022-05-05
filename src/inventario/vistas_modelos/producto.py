from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from artemangaweb.mixins import MensajeResultadoFormMixin
from cuenta_usuario.enums.opciones import TipoUsuario
from cuenta_usuario.restriccion import VistaRestringida

from inventario.models import Producto
from .vistas_genericas import CrearGenerico, ActualizarGenerico, EliminarGenerico
from inventario.forms import ProductoBodegaForm, ActualizarProductoVentasForm


class ProductoListView(ListView):
    model = Producto
    template_name = 'administración/CRUD/listado_producto.html'
    paginate_by = 10
    ordering = ['pk']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contexto_extra = {
            'url_crear': 'crear-producto',
            'url_editar': 'editar-producto',
            'url_eliminar': 'eliminar-producto',
        }

        context.update(contexto_extra)
        return context


class ProductoUpdateView(ActualizarGenerico):
    model = Producto
    fields = None
    form_class = ProductoBodegaForm
    success_url = reverse_lazy('listado-producto')


class ProductoCreateView(CrearGenerico):
    model = Producto
    fields = None
    form_class = ProductoBodegaForm
    success_url = reverse_lazy('listado-producto')


class ProductoDeleteView(EliminarGenerico):
    model = Producto
    success_url = reverse_lazy('listado-producto')


class ActualizarProductoVentasView(VistaRestringida, MensajeResultadoFormMixin, UpdateView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    template_name = 'administración/CRUD/form_generico.html'
    model = Producto
    form_class = ActualizarProductoVentasForm
    success_url = reverse_lazy('ventas-listado-productos')


class VentasListadoProductosView(VistaRestringida, ListView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    model = Producto
    template_name = "administración/ventas/listado_productos.html"
    queryset = Producto.objects.all()
    ordering = ['esta_publicado']
    paginate_by = 10
    context_object_name = 'productos'
