from django.shortcuts import render
from inventario.models import Autor, Genero, Pais, Editorial, OtrosAutores, IVA, Producto
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

class AutorListView(ListView):
    model = Autor
    context_object_name = 'Autores'
    template_name = 'listado_base.html'



def crud_crear_autor(request):
    data = {
        'form': AutorForm()
    }

    if request.method == 'POST':
        formulario = AutorForm(request.POST)

        if formulario.is_valid:
            formulario.save()

        data = {
            'mensaje': 'Usuario escrito satisfactoriamente'
        }
    return render(request, 'inventario/crear_generico.html', data)


def crud_modificar_autor(request, id):
    autor = Autor.objects.get(id=id)
    data = {
        'form': AutorForm(instance=autor)
    }

    if request.method == 'POST':
        formulario = AutorChangeForm(data=request.POST, instance=autor)

        if formulario.is_valid:
            formulario.save()

        data = {
            'mensaje': f'Usuario {autor.nombre} fue modificado con éxito'
        }
    # modificar
    return render(request, 'inventario/listado_base.html', data)


def crud_eliminar_autor(request, id):
    autor = Autor.objects.get(id=id)
    autor.delete()
    return redirect(AutorListView)


class GeneroListView(ListView):
    model = Genero
    context_object_name = 'Generos'
    template_name = 'listado_base.html'


def crud_crear_genero(request, nombre):
    genero = Genero.objects.get(nombre=nombre)
    data = {
        'form': GeneroForm(instance=genero)
    }

    if request.method == 'POST':
        formulario = GeneroForm(data=request.POST, instance=genero)

        if formulario.is_valid:
            formulario.save()

        data = {
            'mensaje': f'Genero {genero.nombre} fue modificado con éxito'
        }
    # modificar
    return render(request, 'inventario/crear_generico.html', data)


def crud_modificar_genero(request, nombre):
    genero = Genero.objects.get(nombre=nombre)
    data = {
        'form': GeneroChangeForm(instance=genero)
    }
    return render(request, 'listado.html', contexto)

    if request.method == 'POST':
        formulario = GeneroChangeForm(data=request.POST, instance=genero)

        if formulario.is_valid:
            formulario.save()

        data = {
            'mensaje': f'Genero {genero.nombre} fue modificado con éxito'
        }
    # modificar
    return render(request, 'inventario/listado_base.html', data)


def crud_eliminar_genero(request, nombre):
    genero = Genero.objects.get(nombre=nombre)
    genero.delete()
    return redirect(GeneroListView)


class PaisListView(ListView):
    model = Pais
    context_object_name = 'Paises'
    template_name = 'listado_base.html'


def crud_crear_pais(request, nombre):
    pais = Pais.objects.get(nombre=nombre)
    data = {
        'form': PaisForm(instance=pais)
    }

    if request.method == 'POST':
        formulario = PaisForm(data=request.POST, instance=pais)

        if formulario.is_valid:
            formulario.save()

        data = {
            'mensaje': f'Pais {pais.nombre} fue modificado con éxito'
        }
    # modificar
    return render(request, 'inventario/crear_generico.html', data)


def crud_modificar_pais(request, nombre):
    pais = Pais.objects.get(nombre=nombre)
    data = {
        'form': PaisChangeForm(instance=pais)
    }

    if request.method == 'POST':
        formulario = PaisChangeForm(data=request.POST, instance=pais)

        if formulario.is_valid:
            formulario.save()

        data = {
            'mensaje': f'Pais {pais.nombre} fue modificado con éxito'
        }
    # modificar
    return render(request, 'inventario/listado_base.html', data)


def crud_eliminar_pais(request, nombre):
    pais = Pais.objects.get(nombre=nombre)
    pais.delete()
    return redirect(PaisListView)


class EditorialListView(ListView):
    model = Editorial
    context_object_name = 'Editoriales'
    template_name = 'listado_base.html'


class OtrosAutoresListView(ListView):
    model = OtrosAutores
    context_object_name = 'Otros Autores'
    template_name = 'listado_base.html'


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
    return render(request, 'listado_base.html', contexto)


class IVAListView(ListView):
    model = IVA
    context_object_name = 'IVA'
    template_name = 'listado_base.html'


class ProductoListView(ListView):
    model = Producto
    context_object_name = 'Productos'
    template_name = 'listado_base.html'


class ProductoList(ListView):
    model = Producto
    template_name = 'CRUD/listado_producto.html'
    paginate_by = 10
    # context_object_name = 'productos'