from django.views.generic import CreateView, UpdateView, DeleteView

FORM_TEMPLATE = 'administración/CRUD/form_generico.html'
ELIMINAR_TEMPLATE = 'administración/CRUD/eliminar_generico.html'


class CrearGenerico(CreateView):
    fields = '__all__'
    template_name = FORM_TEMPLATE


class ActualizarGenerico(UpdateView):
    fields = '__all__'
    template_name = FORM_TEMPLATE


class EliminarGenerico(DeleteView):
    template_name = ELIMINAR_TEMPLATE
