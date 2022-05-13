from django.urls import reverse_lazy

from artemangaweb.mixins import VistaRestringidaMixin
from cuenta_usuario.enums.opciones import TipoUsuario
from inventario.forms import ProductoBodegaForm, ActualizarProductoVentasForm
from inventario.models import Producto
from .vistas_genericas import CrearGenericoView, ActualizarGenericoView, EliminarGenericoView, ListaGenericaView


class ProductoListView(VistaRestringidaMixin, ListaGenericaView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Producto
    template_name = 'administración/CRUD/tabla_producto.html'
    ordering = ['pk']

    tabla_cabecera = ['PK', 'ISBN', 'Título Esp', 'Título Jap', 'Autor', 'Stock', 'Precio', 'Precio sin IVA']


class ProductoUpdateView(VistaRestringidaMixin, ActualizarGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Producto
    fields = None
    form_class = ProductoBodegaForm
    success_url = reverse_lazy('listado-producto')


class ProductoCreateView(VistaRestringidaMixin, CrearGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Producto
    fields = None
    form_class = ProductoBodegaForm
    success_url = reverse_lazy('listado-producto')


class ProductoDeleteView(VistaRestringidaMixin, EliminarGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Producto
    success_url = reverse_lazy('listado-producto')


class ActualizarProductoVentasView(VistaRestringidaMixin, ActualizarGenericoView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    template_name = 'administración/CRUD/form_generico.html'
    model = Producto
    fields = None
    form_class = ActualizarProductoVentasForm
    success_url = reverse_lazy('ventas-listado-productos')


class ProductoVentasListView(VistaRestringidaMixin, ListaGenericaView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    model = Producto
    template_name = "administración/ventas/tabla_productos.html"
    ordering = ['esta_publicado']
    context_object_name = 'productos'
    tabla_cabecera = ['PK', 'Titulo', 'Autor', 'Editorial', 'Generos', 'Precio',
                      'Stock', 'Destacado', 'Publicado', 'Nuevo', 'Editar'
                      ]
    tabla_boton_crear = None
    tabla_boton_eliminar = None
    tabla_boton_editar = 'ventas-actualizar-producto'
