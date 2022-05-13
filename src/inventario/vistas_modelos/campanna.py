from artemangaweb.mixins import VistaRestringidaMixin
from catalogo.models import Campanna
from inventario.vistas_modelos.vistas_genericas import ListaGenericaView, ActualizarGenericoView, EliminarGenericoView, CrearGenericoView
from cuenta_usuario.enums.opciones import TipoUsuario
from django.urls import reverse_lazy

EXITO_URL = reverse_lazy('listado-campannas')

class CampannaListView(VistaRestringidaMixin, ListaGenericaView):
    model = Campanna
    template_name = 'administración/ventas/tabla_campannas.html'
    ordering = ['estado', 'nombre']
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    tabla_cabecera = ['Nombre', 'Estado', 'Redirige a', 'Fecha de expiración']
    context_object_name = 'campannas'



class EditarCampannaView(VistaRestringidaMixin, ActualizarGenericoView):
    model = Campanna
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    success_url = EXITO_URL


class CrearCampannaView(VistaRestringidaMixin, CrearGenericoView):
    model = Campanna
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    success_url = EXITO_URL


class EliminarCampannaView(VistaRestringidaMixin, EliminarGenericoView):
    model = Campanna
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    success_url = EXITO_URL