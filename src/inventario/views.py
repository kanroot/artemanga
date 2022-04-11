from django.shortcuts import render
from inventario.models import Autor, Genero, Pais, Editorial, OtrosAutores, IVA, Producto


# Create your views here.
def index(request):
    autor = Autor.objects.all()
    genero = Genero.objects.all()
    pais = Pais.objects.all()
    editorial = Editorial.objects.all()
    otros_autores = OtrosAutores.objects.all()
    iva = IVA.objects.all()
    producto = Producto.objects.all()
    return render(request, 'crud_autor.html', {"autores": autor})


def crud_autor(request):
    autor = Autor.objects.all()
    contexto = {
        'cabeceras':
            [
                'Nombre',
                'Apellido',
                'Es_activo'
            ],
        'filas':
            [

            ]
    }
    return render(request, 'crud_autor.html', {"autores": autor})
