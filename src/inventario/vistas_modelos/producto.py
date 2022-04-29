from django.urls import reverse_lazy
from django.views.generic import ListView

from inventario.models import Producto
from .vistas_genericas import CrearGenerico, ActualizarGenerico, EliminarGenerico
from inventario.forms import ProductoBodegaForm


class ProductoListView(ListView):
    model = Producto
    template_name = 'CRUD/listado_producto.html'
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
