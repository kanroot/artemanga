from django.urls import reverse_lazy
from django.views.generic import ListView

from inventario.models import Autor

from .vistas_genericas import CrearGenerico, ActualizarGenerico, EliminarGenerico

EXITO_URL = reverse_lazy('listado-autor')


class AutorListView(ListView):
    model = Autor
    context_object_name = 'Autores'
    template_name = 'administración/CRUD/listado_autor.html'
    paginate_by = 10
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contexto_extra = {
            'url_crear': 'crear-autor',
            'url_editar': 'editar-autor',
            'url_eliminar': 'eliminar-autor',
        }

        context.update(contexto_extra)
        return context


class AutorCreateView(CrearGenerico):
    model = Autor
    success_url = EXITO_URL


class AutorUpdateView(ActualizarGenerico):
    model = Autor
    success_url = EXITO_URL


class AutorDeleteView(EliminarGenerico):
    model = Autor
    success_url = EXITO_URL
