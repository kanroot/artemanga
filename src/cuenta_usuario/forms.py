from django import forms
from cuenta_usuario.models import Usuario
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    # Se define el modelo de datos que se va a utilizar en el formulario
    sexo = forms.ChoiceField(label='Sexo',
                             choices=((1, 'Masculino'), (2, 'Femenino'), (3, 'Otro'), (4, 'No deseo responder')),
                             required=False)

    class Meta:
        model = Usuario
        fields = ['username', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'email', 'sexo',
                  'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'email', 'sexo']

