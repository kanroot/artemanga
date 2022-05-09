from django.urls import reverse_lazy

from artemangaweb.mixins import VistaRestringidaMixin
from cuenta_usuario.enums.opciones import TipoUsuario
from inventario.models import Editorial
from .vistas_genericas import CrearGenericoView, ActualizarGenericoView, EliminarGenericoView, ListaGenericaView

EXITO_URL = reverse_lazy('listado-editorial')


class EditorialListView(VistaRestringidaMixin, ListaGenericaView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Editorial
    template_name = 'administración/CRUD/listado_editorial.html'
    paginate_by = 10
    ordering = ['id']
    context_object_name = 'editoriales'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contexto_extra = {
            'url_crear': 'crear-editorial',
            'url_editar': 'editar-editorial',
            'url_eliminar': 'eliminar-editorial',
        }

        context.update(contexto_extra)
        return context


class EditorialCreateView(VistaRestringidaMixin, CrearGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Editorial
    success_url = EXITO_URL


class EditorialUpdateView( VistaRestringidaMixin, ActualizarGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Editorial
    success_url = EXITO_URL


class EditorialDeleteView(VistaRestringidaMixin, EliminarGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Editorial
    success_url = EXITO_URL
