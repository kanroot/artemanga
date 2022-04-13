from django.urls import reverse_lazy
from django.views.generic import ListView

from inventario.models import IVA
from .vistas_genericas import CrearGenerico, ActualizarGenerico, EliminarGenerico

EXITO_URL = reverse_lazy('listado-iva')


class IVAListView(ListView):
    model = IVA
    template_name = 'CRUD/listado_iva.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contexto_extra = {
            'url_crear': 'crear-iva',
            'url_editar': 'editar-iva',
            'url_eliminar': 'eliminar-iva',
        }

        context.update(contexto_extra)
        return context


class IVACreateView(CrearGenerico):
    model = IVA
    success_url = EXITO_URL


class IVAUpdateView(ActualizarGenerico):
    model = IVA
    success_url = EXITO_URL


class IVADeleteView(EliminarGenerico):
    model = IVA
    success_url = EXITO_URL
