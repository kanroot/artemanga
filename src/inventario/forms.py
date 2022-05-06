from .models import Producto, Genero
from django import forms


class ProductoBodegaForm(forms.ModelForm):
    fecha_publicacion = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        widget=forms.widgets.DateInput(attrs={'type': 'date'})
    )

    genero = forms.ModelMultipleChoiceField(
        queryset=Genero.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Producto
        exclude = ['es_destacado', 'esta_publicado']


class ActualizarProductoVentasForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['es_nuevo', 'es_destacado', 'esta_publicado', 'precio']
