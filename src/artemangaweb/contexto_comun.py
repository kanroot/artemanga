from datetime import datetime

from inventario.models import Editorial, Genero, Producto
from catalogo.carrito.models import Carrito
from catalogo.models import Oferta
from django.db.models import Q

def obtener_editoriales_y_categorias(request):
    editoriales = Editorial.objects.filter(producto__stock__gte=1, producto__esta_publicado=True)[:8]
    categorias = Genero.objects.all()
    return {'editoriales': editoriales, 'categorias': categorias}

def obtener_nuevos(request):
    nuevos = Producto.objects.filter(esta_publicado=True).filter(es_nuevo=True).order_by('?')[:8]
    return {'nuevos': nuevos}

def obtener_destacados(request):
    destacados = Producto.objects.filter(esta_publicado=True).filter(es_destacado=True).order_by('?')[:8]
    return {'destacados': destacados}

def obtener_carrito(request):
    carrito: Carrito

    if not request.session.get('carrito', None):
        carrito = Carrito()
        request.session['carrito'] = carrito.serializar()

    return {'carrito': request.session['carrito']}