from django.urls import reverse_lazy

from artemangaweb.mixins import VistaRestringidaMixin
from cuenta_usuario.enums.opciones import TipoUsuario
from inventario.models import Autor
from .vistas_genericas import CrearGenericoView, ActualizarGenericoView, EliminarGenericoView, ListaGenericaView

EXITO_URL = reverse_lazy('listado-autor')


class AutorListView(VistaRestringidaMixin, ListaGenericaView):
    model = Autor
    context_object_name = 'Autores'
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
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


class AutorCreateView(VistaRestringidaMixin, CrearGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Autor
    success_url = EXITO_URL


class AutorUpdateView(VistaRestringidaMixin, ActualizarGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Autor
    success_url = EXITO_URL


class AutorDeleteView(VistaRestringidaMixin, EliminarGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Autor
    success_url = EXITO_URL
