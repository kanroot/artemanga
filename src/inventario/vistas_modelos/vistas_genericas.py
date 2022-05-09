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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = f"Listado de {self.nombre_modelo_plural}"

        if self.titulo_pagina:
            context['titulo_pagina'] = self.titulo_pagina

        return context

    @property
    def nombre_modelo_plural(self):
        return self.model._meta.verbose_name_plural.title()
