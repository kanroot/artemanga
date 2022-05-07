from django.urls import reverse_lazy
from django.views.generic import ListView
from inventario.models import Genero
from .vistas_genericas import CrearGenerico, ActualizarGenerico, EliminarGenerico
from artemangaweb.mixins import MensajeResultadoFormMixin, TituloPaginaMixin, VistaRestringidaMixin
from cuenta_usuario.enums.opciones import TipoUsuario

EXITO_URL = reverse_lazy('listado-genero')


class GeneroListView(TituloPaginaMixin, VistaRestringidaMixin, ListView):
    titulo_pagina = 'Listado de Generos'
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    model = Genero
    template_name = 'administración/CRUD/listado_genero.html'
    paginate_by = 10
    ordering = ['id']
    context_object_name = 'generos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contexto_extra = {
            'url_crear': 'crear-genero',
            'url_editar': 'editar-genero',
            'url_eliminar': 'eliminar-genero',
        }

        context.update(contexto_extra)
        return context


class GeneroCreateView(TituloPaginaMixin, MensajeResultadoFormMixin, VistaRestringidaMixin, CrearGenerico):
    titulo_pagina = "Actualizar producto"
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    mensaje_error = "No se pudo crear el genero"
    mensaje_exito = "Se creo el genero correctamente"
    model = Genero
    success_url = EXITO_URL


class GeneroUpdateView(TituloPaginaMixin, MensajeResultadoFormMixin, VistaRestringidaMixin, ActualizarGenerico):
    titulo_pagina = "Actualizar genero"
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    mensaje_error = "No se pudo actualizar el genero"
    mensaje_exito = "Se actualizo el genero correctamente"
    model = Genero
    success_url = EXITO_URL


class GeneroDeleteView(TituloPaginaMixin, MensajeResultadoFormMixin, VistaRestringidaMixin, EliminarGenerico):
    titulo_pagina = "Eliminar genero"
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA]
    mensaje_error = "No se pudo eliminar el genero"
    mensaje_exito = "Se elimino el genero correctamente"
    model = Genero
    success_url = EXITO_URL
