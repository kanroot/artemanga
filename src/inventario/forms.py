from .models import Producto, Genero
from django import forms
from venta.models import Venta
from venta.tipo_enum.estado_venta import EstadoVenta


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
        fields = ['es_destacado', 'esta_publicado', 'precio']


class ValidarTransferenciaForm(forms.Form):
    producto = forms.ModelChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    cantidad = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )


class ValidarVenta(forms.Form):
    venta = forms.ModelChoiceField(
        queryset=Venta.objects.filter(estado=EstadoVenta.PENDIENTE.value),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

