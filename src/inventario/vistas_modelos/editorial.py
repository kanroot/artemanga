from django.urls import reverse_lazy
from django.views.generic import ListView
from cuenta_usuario.enums.opciones import TipoUsuario
from artemangaweb.mixins import MensajeResultadoFormMixin, TituloPaginaMixin, VistaRestringidaMixin
from inventario.models import Editorial
from .vistas_genericas import CrearGenerico, ActualizarGenerico, EliminarGenerico

EXITO_URL = reverse_lazy('listado-editorial')


class EditorialListView(TituloPaginaMixin, VistaRestringidaMixin, ListView):
    titulo_pagina = 'Editoriales'
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


class EditorialCreateView(TituloPaginaMixin, MensajeResultadoFormMixin, VistaRestringidaMixin, CrearGenerico):
    titulo_pagina = 'Crear Editorial'
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Editorial
    mensaje_error = 'No se pudo crear la editorial'
    mensaje_exito = 'Editorial creada con éxito'
    success_url = EXITO_URL


class EditorialUpdateView(TituloPaginaMixin, MensajeResultadoFormMixin, VistaRestringidaMixin, ActualizarGenerico):
    titulo_pagina = 'Actualizar Editorial'
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Editorial
    mensaje_error = 'No se pudo actualizar la editorial'
    mensaje_exito = 'Editorial actualizada con éxito'
    success_url = EXITO_URL


class EditorialDeleteView(TituloPaginaMixin, MensajeResultadoFormMixin, VistaRestringidaMixin, EliminarGenerico):
    titulo_pagina = 'Eliminar Editorial'
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Editorial
    mensaje_error = 'No se pudo eliminar la editorial'
    mensaje_exito = 'Editorial eliminada con éxito'
    success_url = EXITO_URL
