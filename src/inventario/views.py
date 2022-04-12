from django.shortcuts import render, redirect
from inventario.models import Autor, Genero, Pais, Editorial, OtrosAutores, IVA, Producto
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

class AutorListView(ListView):
    model = Autor
    context_object_name = 'Autores'
    template_name = 'CRUD/listado_autor.html'
    paginate_by = 10


class GeneroListView(ListView):
    model = Genero
    context_object_name = 'Generos'
    template_name = 'CRUD/listado_genero.html'
    paginate_by = 10


class PaisListView(ListView):
    model = Pais
    context_object_name = 'Paises'
    template_name = 'CRUD/listado_pais.html'
    paginate_by = 10


class EditorialListView(ListView):
    model = Editorial
    context_object_name = 'Editoriales'
    template_name = 'CRUD/listado_editorial.html'
    paginate_by = 10


class OtrosAutoresListView(ListView):
    model = OtrosAutores
    context_object_name = 'Otros Autores'
    template_name = 'CRUD/listado_otro_autor.html'
    paginate_by = 10


class IVAListView(ListView):
    model = IVA
    context_object_name = 'IVA'
    template_name = 'CRUD/listado_iva.html'
    paginate_by = 10


class ProductoListView(ListView):
    model = Producto
    context_object_name = 'Productos'
    template_name = 'CRUD/listado_producto.html'
    paginate_by = 10