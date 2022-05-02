from django import forms

from .models import Usuario
from django.contrib.auth.forms import UserCreationForm


class RegistroUsuarioForm(UserCreationForm):
    sexo = forms.ChoiceField(
        label='Sexo',
        choices=((4, 'No deseo responder'), (1, 'Masculino'), (2, 'Femenino'), (3, 'Otro'))
    )
    email = forms.EmailField(
        label='Correo electrónico',
        required=True,
    )

    class Meta:
        model = Usuario
        fields = [
            'username', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'email', 'sexo',
            'password1', 'password2']
