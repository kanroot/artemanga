from inventario.models import Editorial, Genero


def obtener_editoriales_y_categorias(request):
    editoriales = Editorial.objects.all()
    categorias = Genero.objects.all()
    return {'editoriales': editoriales, 'categorias': categorias}