from django.urls import reverse_lazy
from django.views.generic import ListView

from inventario.models import Editorial
from .vistas_genericas import CrearGenerico, ActualizarGenerico, EliminarGenerico

EXITO_URL = reverse_lazy('listado-editorial')


class EditorialListView(ListView):
    model = Editorial
    template_name = 'CRUD/listado_editorial.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contexto_extra = {
            'url_crear': 'crear-editorial',
            'url_editar': 'editar-editorial',
            'url_eliminar': 'eliminar-editorial',
        }

        context.update(contexto_extra)
        return context


class EditorialCreateView(CrearGenerico):
    model = Editorial
    success_url = EXITO_URL


class EditorialUpdateView(ActualizarGenerico):
    model = Editorial
    success_url = EXITO_URL


class EditorialDeleteView(EliminarGenerico):
    model = Editorial
    success_url = EXITO_URL
