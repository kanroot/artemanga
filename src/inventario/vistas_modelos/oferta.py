from catalogo.models import Oferta
from .vistas_genericas import CrearGenericoView, ActualizarGenericoView, EliminarGenericoView, ListaGenericaView
from django.urls import reverse_lazy
from artemangaweb.mixins import VistaRestringidaMixin
from cuenta_usuario.enums.opciones import TipoUsuario
from inventario.forms import OfertaForm

class OfertaListView(VistaRestringidaMixin, ListaGenericaView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    model = Oferta
    context_object_name = 'ofertas'
    tabla_cabecera = ['ID', 'Producto', 'Descuento', 'Es válida']
    ordering = ['-id']
    template_name = 'administración/ventas/tabla_ofertas.html'


class OfertaCreateView(VistaRestringidaMixin, CrearGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    model = Oferta
    template_name = 'administración/CRUD/form_generico.html'
    success_url = reverse_lazy('listado-ofertas')
    form_class = OfertaForm
    fields = None

class OfertaUpdateView(VistaRestringidaMixin, ActualizarGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    model = Oferta
    form_class = OfertaForm
    template_name = 'administración/CRUD/form_generico.html'
    success_url = reverse_lazy('listado-ofertas')
    fields = None


class OfertaDeleteView(VistaRestringidaMixin, EliminarGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    model = Oferta
    template_name = 'administración/CRUD/eliminar_generico.html'
    success_url = reverse_lazy('listado-ofertas')
