from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from cuenta_usuario.enums.opciones import TipoUsuario
from inventario.models import Producto
from .vistas_genericas import CrearGenerico, ActualizarGenerico, EliminarGenerico
from inventario.forms import ProductoBodegaForm, ActualizarProductoVentasForm
from artemangaweb.mixins import MensajeResultadoFormMixin, TituloPaginaMixin, VistaRestringidaMixin


class ProductoListView(TituloPaginaMixin, VistaRestringidaMixin, ListView):
    titulo_pagina = "Productos en inventario"
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Producto
    template_name = 'administración/CRUD/listado_producto.html'
    paginate_by = 10
    ordering = ['pk']
    context_object_name = 'productos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contexto_extra = {
            'url_crear': 'crear-producto',
            'url_editar': 'editar-producto',
            'url_eliminar': 'eliminar-producto',
        }

        context.update(contexto_extra)
        return context


class ProductoUpdateView(TituloPaginaMixin, MensajeResultadoFormMixin, VistaRestringidaMixin, ActualizarGenerico):
    titulo_pagina = "Actualizar producto"
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Producto
    fields = None
    mensaje_error = "No se pudo actualizar el producto"
    mensaje_exito = "Producto actualizado correctamente"
    form_class = ProductoBodegaForm
    success_url = reverse_lazy('listado-producto')


class ProductoCreateView(TituloPaginaMixin, MensajeResultadoFormMixin, VistaRestringidaMixin, CrearGenerico):
    titulo_pagina = 'Crear producto'
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Producto
    fields = None
    mensaje_error = "No se pudo crear el producto"
    mensaje_exito = "Producto creado correctamente"
    form_class = ProductoBodegaForm
    success_url = reverse_lazy('listado-producto')


class ProductoDeleteView(TituloPaginaMixin, MensajeResultadoFormMixin, VistaRestringidaMixin, EliminarGenerico):
    titulo_pagina = "Confirmar eliminación de producto"
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Producto
    mensaje_error = "No se pudo eliminar el producto"
    mensaje_exito = "Producto eliminado correctamente"
    success_url = reverse_lazy('listado-producto')


class ActualizarProductoVentasView(VistaRestringidaMixin, MensajeResultadoFormMixin, UpdateView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    template_name = 'administración/CRUD/form_generico.html'
    model = Producto
    form_class = ActualizarProductoVentasForm
    success_url = reverse_lazy('ventas-listado-productos')


class VentasListadoProductosView(VistaRestringidaMixin, ListView):
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.VENTAS]
    model = Producto
    template_name = "administración/ventas/listado_productos.html"
    queryset = Producto.objects.all()
    ordering = ['esta_publicado']
    paginate_by = 10
    context_object_name = 'productos'
