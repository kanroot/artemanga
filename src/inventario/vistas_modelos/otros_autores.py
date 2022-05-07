from django.urls import reverse_lazy
from django.views.generic import ListView

from inventario.models import OtrosAutores
from .vistas_genericas import CrearGenerico, ActualizarGenerico, EliminarGenerico
from artemangaweb.mixins import MensajeResultadoFormMixin, TituloPaginaMixin, VistaRestringidaMixin
from cuenta_usuario.enums.opciones import TipoUsuario

URL_EXITO = reverse_lazy('listado-otro-autor')


class OtrosAutoresListView(TituloPaginaMixin, VistaRestringidaMixin, ListView):
    titulo_pagina = 'Listado de otros autores'
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


class OtrosAutoresCreateView(TituloPaginaMixin, MensajeResultadoFormMixin, VistaRestringidaMixin, CrearGenerico):
    titulo_pagina = 'Crear otro autor'
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    mensaje_error = "No se pudo crear el Otro Autor"
    mensaje_exito = "Otro Autor creado con éxito"
    model = OtrosAutores
    success_url = URL_EXITO


class OtrosAutoresUpdateView(TituloPaginaMixin, MensajeResultadoFormMixin, VistaRestringidaMixin, ActualizarGenerico):
    titulo_pagina = 'Actualizar otro autor'
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    mensaje_error = "No se pudo actualizar el Otro Autor"
    mensaje_exito = "Otro Autor actualizado con éxito"
    model = OtrosAutores
    success_url = URL_EXITO


class OtrosAutoresDeleteView(TituloPaginaMixin, MensajeResultadoFormMixin, VistaRestringidaMixin, EliminarGenerico):
    titulo_pagina = 'Eliminar otro autor'
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    mensaje_error = "No se pudo eliminar el Otro Autor"
    mensaje_exito = "Otro Autor eliminado con éxito"
    model = OtrosAutores
    success_url = URL_EXITO
