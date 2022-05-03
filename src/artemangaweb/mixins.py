from django.contrib import messages


class MensajeResultadoFormMixin:
    mensaje_exito = 'Operación realizada con éxito'
    mensaje_error = 'Ha ocurrido un error'

    def form_valid(self, form):
        messages.success(self.request, self.mensaje_exito)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.mensaje_error)
        return super().form_invalid(form)


class TituloPaginaMixin(object):
    def get_page_title(self, context):
        return getattr(self, "titulo_pagina", "Default Page Title")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = self.get_page_title(context)

        return context
