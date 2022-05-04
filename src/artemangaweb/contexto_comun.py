from inventario.models import Editorial, Genero, Producto
from catalogo.carrito.models import Carrito


def obtener_editoriales_y_categorias(request):
    editoriales = Editorial.objects.all()
    categorias = Genero.objects.all()
    return {'editoriales': editoriales, 'categorias': categorias}

def obtener_nuevos(request):
    nuevos = Producto.objects.filter(esta_publicado=True).filter(es_nuevo=True)
    return {'nuevos': nuevos}

def obtener_destacados(request):
    destacados = Producto.objects.filter(esta_publicado=True).filter(es_destacado=True)
    return {'destacados': destacados}

def obtener_carrito(request):
    carrito: Carrito

    if not request.session.get('carrito', None):
        carrito = Carrito()
        request.session['carrito'] = carrito.serializar()

    return {'carrito': request.session['carrito']}