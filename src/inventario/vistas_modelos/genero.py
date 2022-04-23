from django.urls import reverse_lazy
from django.views.generic import ListView
from inventario.models import Genero
from .vistas_genericas import CrearGenerico, ActualizarGenerico, EliminarGenerico

EXITO_URL = reverse_lazy('listado-genero')


class GeneroListView(ListView):
    model = Genero
    template_name = 'CRUD/listado_genero.html'
    paginate_by = 10
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contexto_extra = {
            'url_crear': 'crear-genero',
            'url_editar': 'editar-genero',
            'url_eliminar': 'eliminar-genero',
        }

        context.update(contexto_extra)
        return context


class GeneroCreateView(CrearGenerico):
    model = Genero
    success_url = EXITO_URL


class GeneroUpdateView(ActualizarGenerico):
    model = Genero
    success_url = EXITO_URL


class GeneroDeleteView(EliminarGenerico):
    model = Genero
    success_url = EXITO_URL
