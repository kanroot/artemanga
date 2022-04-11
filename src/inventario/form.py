from .models import Autor
from django import forms


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'es_activo']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'es_activo': 'Activo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'es_activo': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

