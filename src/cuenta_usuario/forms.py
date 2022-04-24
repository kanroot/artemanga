from django.views.generic import CreateView, UpdateView
from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    # Se define el modelo de datos que se va a utilizar en el formulario
    sexo = forms.ChoiceField(label='Sexo',
                             choices=((1, 'Masculino'), (2, 'Femenino'), (3, 'Otro'), (4, 'No deseo responder')),
                             required=False)

    class Meta:
        model = Usuario
        fields = ['username', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'email', 'sexo',
                  'password1', 'password2']


class UserRegisterForm(CreateView):
    model = Usuario
    template_name = 'generico_form.html'
    form_class = UserForm
    success_message = "Tú perfil ha sido creado con éxito"


class UserUpdateForm(UpdateView):
    model = Usuario
    template_name = 'generico_form.html'
    fields = ['primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'sexo']
    success_message = "Tú perfil ha sido modificado con éxito"
