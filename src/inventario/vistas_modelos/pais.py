from django.urls import reverse_lazy
from django.views.generic import ListView

from inventario.models import Pais
from .vistas_genericas import CrearGenerico, ActualizarGenerico, EliminarGenerico


EXITO_URL = reverse_lazy('listado-pais')


class PaisListView(ListView):
    model = Pais
    template_name = 'CRUD/listado_pais.html'
    paginate_by = 10
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contexto_extra = {
            'url_crear': 'crear-pais',
            'url_editar': 'editar-pais',
            'url_eliminar': 'eliminar-pais',
        }

        context.update(contexto_extra)
        return context


class PaisCreateView(CrearGenerico):
    model = Pais
    success_url = EXITO_URL


class PaisUpdateView(ActualizarGenerico):
    model = Pais
    success_url = EXITO_URL


class PaisDeleteView(EliminarGenerico):
    model = Pais
    success_url = EXITO_URL
