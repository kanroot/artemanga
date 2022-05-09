from django.urls import reverse_lazy

from artemangaweb.mixins import VistaRestringidaMixin
from cuenta_usuario.enums.opciones import TipoUsuario
from inventario.models import Pais
from .vistas_genericas import CrearGenericoView, ActualizarGenericoView, EliminarGenericoView, ListaGenericaView

EXITO_URL = reverse_lazy('listado-pais')


class PaisListView(VistaRestringidaMixin, ListaGenericaView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    context_object_name = 'paises'
    model = Pais
    template_name = 'administración/CRUD/listado_pais.html'
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


class PaisCreateView(VistaRestringidaMixin, CrearGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Pais
    success_url = EXITO_URL


class PaisUpdateView(VistaRestringidaMixin, ActualizarGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Pais
    success_url = EXITO_URL


class PaisDeleteView(VistaRestringidaMixin, EliminarGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Pais
    success_url = EXITO_URL
