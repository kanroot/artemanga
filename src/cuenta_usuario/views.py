from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import UserRegisterForm, UserUpdateForm


# Create your views here.
class SignUpView(CreateView):
    template_name = 'registro.html'
    success_url = '/'
    form_class = UserRegisterForm
    success_message = "Tú perfil ha sido creado con éxito"


class ModifyProfileView(UpdateView):
    template_name = 'modificar_perfil.html'
    success_url = '/'
    form_class = UserUpdateForm
    success_message = "Tú perfil ha sido modificado con éxito"



