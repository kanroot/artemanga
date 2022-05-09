from django.urls import reverse_lazy

from artemangaweb.mixins import VistaRestringidaMixin
from cuenta_usuario.enums.opciones import TipoUsuario
from inventario.models import OtrosAutores
from .vistas_genericas import CrearGenericoView, ActualizarGenericoView, EliminarGenericoView, ListaGenericaView

URL_EXITO = reverse_lazy('listado-otro-autor')


class OtrosAutoresListView(VistaRestringidaMixin, ListaGenericaView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = OtrosAutores
    template_name = 'administración/CRUD/listado_otro_autor.html'
    paginate_by = 10
    ordering = ['id']
    context_object_name = 'otros_autores'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contexto_extra = {
            'url_crear': 'crear-otro-autor',
            'url_editar': 'editar-otro-autor',
            'url_eliminar': 'eliminar-otro-autor',
        }

        context.update(contexto_extra)
        return context


class OtrosAutoresCreateView(VistaRestringidaMixin, CrearGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = OtrosAutores
    success_url = URL_EXITO


class OtrosAutoresUpdateView(VistaRestringidaMixin, ActualizarGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = OtrosAutores
    success_url = URL_EXITO


class OtrosAutoresDeleteView(VistaRestringidaMixin, EliminarGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = OtrosAutores
    success_url = URL_EXITO
