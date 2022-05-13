from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from artemangaweb.mixins import MensajeResultadoFormMixin, TituloPaginaMixin

FORM_TEMPLATE = 'administración/CRUD/form_generico.html'
ELIMINAR_TEMPLATE = 'administración/CRUD/eliminar_generico.html'


class CrearGenericoView(TituloPaginaMixin, MensajeResultadoFormMixin, CreateView):
    fields = '__all__'
    template_name = FORM_TEMPLATE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = f"Crear {self.nombre_modelo}"
        return context

    def get_mensaje_exito(self):
        return f"{self.nombre_modelo} creado correctamente"

    def get_mensaje_error(self):
        return f"Error al crear {self.nombre_modelo}"

    @property
    def nombre_modelo(self):
        return self.model._meta.verbose_name.title()


class ActualizarGenericoView(TituloPaginaMixin, MensajeResultadoFormMixin, UpdateView):
    fields = '__all__'
    template_name = FORM_TEMPLATE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = f"Actualizar {self.nombre_modelo}: {self.object}"
        return context

    def get_mensaje_exito(self):
        return f"{self.nombre_modelo} actualizado correctamente"

    def get_mensaje_error(self):
        return f"Error al actualizar {self.nombre_modelo}"

    @property
    def nombre_modelo(self):
        return self.model._meta.verbose_name.title()


class EliminarGenericoView(TituloPaginaMixin, MensajeResultadoFormMixin, DeleteView):
    template_name = ELIMINAR_TEMPLATE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = f"Eliminar {self.nombre_modelo}: {self.object}"
        return context

    def get_mensaje_exito(self):
        return f"{self.nombre_modelo} eliminado correctamente"

    def get_mensaje_error(self):
        return f"Error al eliminar {self.nombre_modelo}"

    @property
    def nombre_modelo(self):
        return self.model._meta.verbose_name.title()


class ListaGenericaView(TituloPaginaMixin, ListView):
    tabla_cabecera: list[str] = []
    tabla_descripcion: str = ''
    tabla_boton_crear: str = ''
    tabla_boton_editar: str = ''
    tabla_boton_eliminar: str = ''
    paginate_by = 10

    @property
    def nombre_modelo_plural(self):
        return self.model._meta.verbose_name_plural.title()

    def get_titulo_pagina(self):
        if self.titulo_pagina:
            return self.titulo_pagina
        return f"Listado de {self.nombre_modelo_plural}"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tabla_cabecera'] = self.tabla_cabecera
        context['tabla_descripcion'] = self.get_tabla_descripcion()
        context['tabla_boton_editar'] = self.get_boton_editar()
        context['tabla_boton_eliminar'] = self.get_boton_eliminar()
        context['tabla_boton_crear'] = self.get_boton_crear()

        return context

    def get_tabla_descripcion(self) -> str:
        if self.tabla_descripcion:
            return self.tabla_descripcion

        texto = f'Se presenta un listado de {self.nombre_modelo_plural}.'
        orden = self.get_ordering()
        if orden:
            texto += f' Los resultados se ordenan por {orden}'
            if '-' in orden:
                texto += ' en orden descendente.'
            else:
                texto += ' en orden ascendente.'
        return texto

    def get_boton_crear(self) -> str | None:
        if self.tabla_boton_crear or self.tabla_boton_crear is None:
            return self.tabla_boton_crear
        return self.intentar_obtener_boton('crear')

    def get_boton_editar(self) -> str | None:
        if self.tabla_boton_editar or self.tabla_boton_editar is None:
            return self.tabla_boton_editar
        return self.intentar_obtener_boton('editar')

    def get_boton_eliminar(self) -> str | None:
        if self.tabla_boton_eliminar or self.tabla_boton_eliminar is None:
            return self.tabla_boton_eliminar
        return self.intentar_obtener_boton('eliminar')

    def intentar_obtener_boton(self, accion: str) -> str:
        return f"{accion}-{self.model._meta.model_name.lower()}"






