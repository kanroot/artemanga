from django.urls import reverse_lazy

from artemangaweb.mixins import VistaRestringidaMixin
from cuenta_usuario.enums.opciones import TipoUsuario
from inventario.models import OtrosAutores
from .vistas_genericas import CrearGenericoView, ActualizarGenericoView, EliminarGenericoView, ListaGenericaView

URL_EXITO = reverse_lazy('listado-otro-autor')


class OtrosAutoresListView(VistaRestringidaMixin, ListaGenericaView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = OtrosAutores
    template_name = 'administración/CRUD/tabla_otros_autores.html'
    ordering = ['id']
    context_object_name = 'otros_autores'
    tabla_cabecera = ['ID', 'Nombre', 'Cargo']
    tabla_boton_crear = 'crear-otro-autor'
    tabla_boton_editar = 'editar-otro-autor'
    tabla_boton_eliminar = 'eliminar-otro-autor'


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
