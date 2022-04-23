from django import forms
from cuenta_usuario.models import Usuario
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    # Se define el modelo de datos que se va a utilizar en el formulario
    primer_nombre = forms.CharField(label='Primer Nombre')
    segundo_nombre = forms.CharField(label='Segundo Nombre', required=False)
    primer_apellido = forms.CharField(label='Primer Apellido')
    segundo_apellido = forms.CharField(label='Segundo Apellido', required=False)
    email = forms.EmailField(label='Correo Electrónico')
    sexo = forms.ChoiceField(label='Sexo',
                             choices=(('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')),
                             required=False)

    class Meta:
        model = Usuario
        fields = ['primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'email', 'sexo',
                  'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'email', 'sexo']


class DeleteUserForm(forms.ModelForm):
    class Meta:
        model = Usuario

