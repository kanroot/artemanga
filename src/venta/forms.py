from django import forms
from .models import Direccion
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class CrearDireccionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()

    class Meta:
        model = Direccion
        fields = '__all__'


class ElegirDireccionForm(forms.Form):
    direccion = forms.ModelChoiceField(queryset=Direccion.objects.none())
    usuario = None

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario')
        super().__init__(*args, **kwargs)
        self.fields['direccion'].queryset = Direccion.objects.filter(usuario=self.usuario)
        self.helper = FormHelper()
        self.helper.form_class = 'd-grid gap-2'
        self.helper.layout = Layout(
            Fieldset(
                '¿A dónde te mandamos tu pedido?',
                'direccion',
                ButtonHolder(
                    Submit('submit', 'Quiero esta dirección', css_class='btn-primary')
                )
            )
        )
