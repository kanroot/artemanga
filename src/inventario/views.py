from django.shortcuts import render, redirect
from inventario.models import Autor, Genero, Pais, Editorial, OtrosAutores, IVA, Producto
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

class AutorListView(ListView):
    model = Autor
    context_object_name = 'Autores'
    template_name = 'CRUD/listado_autor.html'
    paginate_by = 10


class AutorCreateView(CreateView):
    model = Autor
    fields = ['nombre', 'apellido', 'es_activo']


class GeneroListView(ListView):
    model = Genero
    context_object_name = 'Generos'
    template_name = 'CRUD/listado_genero.html'
    paginate_by = 10


class GeneroCreateView(CreateView):
    model = Genero
    fields = ['nombre']


class PaisListView(ListView):
    model = Pais
    context_object_name = 'Paises'
    template_name = 'CRUD/listado_pais.html'
    paginate_by = 10


class PaisCreateView(CreateView):
    model = Pais
    fields = ['nombre']


class EditorialListView(ListView):
    model = Editorial
    context_object_name = 'Editoriales'
    template_name = 'CRUD/listado_editorial.html'
    paginate_by = 10


class EditorialCreateView(CreateView):
    model = Editorial
    fields = ['nombre']


class OtrosAutoresListView(ListView):
    model = OtrosAutores
    context_object_name = 'Otros Autores'
    template_name = 'CRUD/listado_otro_autor.html'
    paginate_by = 10


class OtrosAutoresCreateView(CreateView):
    model = OtrosAutores
    fields = ['nombre', 'cargo']


class IVAListView(ListView):
    model = IVA
    context_object_name = 'IVA'
    template_name = 'CRUD/listado_iva.html'
    paginate_by = 10


class IVACreateView(CreateView):
    model = IVA
    fields = ['iva']


class ProductoListView(ListView):
    model = Producto
    context_object_name = 'Productos'
    template_name = 'CRUD/listado_producto.html'
    paginate_by = 10


class ProductoCreateView(CreateView):
    model = Producto
    fields = ['isbn',
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
