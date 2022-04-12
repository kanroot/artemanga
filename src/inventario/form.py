from .models import Autor, Genero, Pais, Editorial, OtrosAutores, IVA, Producto
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


class AutorChangeForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'es_activo']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'es_activo': 'Activo',
        }


class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }


class GeneroChangeForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre',
        }


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PaisChangeForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre',
        }


class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditorialChangeForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre',
        }


class OtrosAutoresForm(forms.Form):
    class Meta:
        model = OtrosAutores
        fields = ['nombre', 'cargo']
        labels = {
            'nombre': 'Nombre',
            'cargo': 'Cargo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
        }


class OtrosAutoresChangeForm(forms.ModelForm):
    class Meta:
        model = OtrosAutores
        fields = ['nombre', 'cargo']
        labels = {
            'nombre': 'Nombre',
            'cargo': 'Cargo',
        }


class IVAForm(forms.ModelForm):
    class Meta:
        model = IVA
        fields = ['iva', ]
        labels = {
            'iva': 'IVA',
        }
        widgets = {
            'iva': forms.TextInput(attrs={'class': 'form-control'}),
        }


class IVAChangeForm(forms.ModelForm):
    class Meta:
        model = IVA
        fields = ['iva', ]
        labels = {
            'iva': 'IVA',
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'titulo_es',
            'titulo_jp',
            'stock',
            'portada',
            'precio',
            'descripcion',
            'numero_paginas',
            'es_color',
            'fecha_publicacion',
            'esta_publicado',
            'es_destacado']
        labels = {
            'titulo_es': 'Título en español',
            'titulo_jp': 'Título en japonés',
            'stock': 'Stock',
            'portada': 'Portada',
            'precio': 'Precio',
            'descripcion': 'Descripción',
            'numero_paginas': 'Número de páginas',
            'es_color': 'Color',
            'fecha_publicacion': 'Fecha de publicación',
            'esta_publicado': 'Está publicado',
            'es_destacado': 'Destacado',

        }
        widgets = {
            'titulo_es': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo_jp': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.TextInput(attrs={'class': 'form-control'}),
            'portada': forms.FileInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'numero_paginas': forms.TextInput(attrs={'class': 'form-control'}),
            'es_color': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control'}),
            'esta_publicado': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'es_destacado': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }


class ProductoChangeForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'titulo_es',
            'titulo_jp',
            'stock',
            'portada',
            'precio',
            'descripcion',
            'numero_paginas',
            'es_color',
            'fecha_publicacion',
            'esta_publicado',
            'es_destacado']
