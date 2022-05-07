from django.urls import reverse_lazy
from django.views.generic import ListView
from inventario.models import Pais
from .vistas_genericas import CrearGenerico, ActualizarGenerico, EliminarGenerico
from artemangaweb.mixins import MensajeResultadoFormMixin, TituloPaginaMixin, VistaRestringidaMixin
from cuenta_usuario.enums.opciones import TipoUsuario

EXITO_URL = reverse_lazy('listado-pais')


class PaisListView(TituloPaginaMixin, VistaRestringidaMixin, ListView):
    titulo_pagina = 'Listado de Países'
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


class PaisCreateView(TituloPaginaMixin, MensajeResultadoFormMixin, VistaRestringidaMixin, CrearGenerico):
    titulo_pagina = 'Crear País'
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    mensaje_error = 'No se pudo crear el país'
    mensaje_exito = 'País creado con éxito'
    model = Pais
    success_url = EXITO_URL


class PaisUpdateView(TituloPaginaMixin, MensajeResultadoFormMixin, VistaRestringidaMixin, ActualizarGenerico):
    titulo_pagina = 'Actualizar País'
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    mensaje_error = 'No se pudo actualizar el país'
    mensaje_exito = 'País actualizado con éxito'
    model = Pais
    success_url = EXITO_URL


class PaisDeleteView(TituloPaginaMixin, MensajeResultadoFormMixin, VistaRestringidaMixin, EliminarGenerico):
    titulo_pagina = 'Eliminar País'
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    mensaje_error = 'No se pudo eliminar el país'
    mensaje_exito = 'País eliminado con éxito'
    model = Pais
    success_url = EXITO_URL
