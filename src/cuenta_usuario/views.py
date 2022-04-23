from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from cuenta_usuario.forms import UserRegisterForm


# Create your views here.
class SignUpView(CreateView):
    template_name = 'cuenta_usuario/templates/registro.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Tú perfil ha sido creado con éxito"


class ModifyProfileView(CreateView):
    template_name = 'cuenta_usuario/templates/modificar_perfil.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Tú perfil ha sido modificado con éxito"


class DeleteProfileView(CreateView):
    template_name = 'cuenta_usuario/templates/eliminar_perfil.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Tú perfil ha sido eliminado con éxito"
