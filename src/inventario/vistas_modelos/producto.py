from django.urls import reverse_lazy
from django.views.generic import ListView

from inventario.models import Producto
from .vistas_genericas import CrearGenerico, ActualizarGenerico, EliminarGenerico


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
    success_url = reverse_lazy('listado-producto')
    fields = '__all__'


class ProductoCreateView(CrearGenerico):
    model = Producto
    success_url = reverse_lazy('listado-producto')
    fields = '__all__'


class ProductoDeleteView(EliminarGenerico):
    model = Producto
    success_url = reverse_lazy('listado-producto')
