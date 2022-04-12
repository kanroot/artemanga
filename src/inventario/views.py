from django.shortcuts import render
from inventario.models import Autor, Genero, Pais, Editorial, OtrosAutores, IVA, Producto
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

def crud_autor(request):
    contexto = {
        'cabeceras':
            [
                'Nombre',
                'Apellido',
                'Es_activo',
                'Modificar',
                'Eliminar'
            ],
        'filas': [[a.nombre, a.apellido, a.es_activo] for a in Autor.objects.all()],
        'titulo': 'Autores'
    }
    return render(request, 'listado.html', contexto)


def crud_genero(request):
    contexto = {
        'cabeceras':
            [
                'Nombre',
                'Modificar',
                'Eliminar'
            ],
        'filas': [[a.nombre] for a in Genero.objects.all()],
        'titulo': 'Generos'
    }
    return render(request, 'listado.html', contexto)


def crud_pais(request):
    contexto = {
        'cabeceras':
            [
                'ID',
                'Nombre'
            ],
        'filas': [[a.id, a.nombre] for a in Pais.objects.all()],
        'titulo': 'Paises'
    }
    return render(request, 'listado.html', contexto)


def crud_editorial(request):
    contexto = {
        'cabeceras':
            [
                'ID',
                'Nombre',
                'Pais'
            ],
        'filas': [[a.id, a.nombre, a.pais] for a in Editorial.objects.all()],
        'titulo': 'Editoriales'
    }
    return render(request, 'listado.html', contexto)


def crud_otros_autores(request):
    contexto = {
        'cabeceras':
            [
                'ID',
                'Nombre',
                'Cargo'
            ],
        'filas': [[a.id, a.nombre, a.cargo] for a in OtrosAutores.objects.all()],
        'titulo': 'Otros autores'
    }
    return render(request, 'listado.html', contexto)


def crud_iva(request):
    contexto = {
        'cabeceras':
            [
                'IVA'
            ],
        'filas': [[a.iva] for a in IVA.objects.all()],
        'titulo': 'IVA'
    }
    return render(request, 'listado.html', contexto)


def crud_producto(request):
    contexto = {
        'cabeceras':
            [
                'ISBN',
                'Titulo español',
                'Titulo japones',
                'Stock',
                'Precio',
                'Descripcion',
                'Numero de paginas',
                'Es color',
                'Fecha de publicacion',
                'Esta publicado',
                'Es destacado'

            ],
        'filas': [[a.isbn, a.titulo_es, a.titulo_jp, a.stock, a.precio, a.descripcion, a.numero_paginas, a.es_color,
                   a.fecha_publicacion, a.esta_publicado, a.es_destacado] for a in Producto.objects.all()],
        'titulo': 'Productos'
    }
    return render(request, 'listado.html', contexto)


class ProductoList(ListView):
    model = Producto
    template_name = 'CRUD/listado_producto.html'
    paginate_by = 10
    # context_object_name = 'productos'