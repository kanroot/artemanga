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

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.primer_nombre = self.cleaned_data['primer_nombre']
        user.segundo_nombre = self.cleaned_data['segundo_nombre']
        user.primer_apellido = self.cleaned_data['primer_apellido']
        user.segundo_apellido = self.cleaned_data['segundo_apellido']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'email', 'sexo']


class DeleteUserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = []
