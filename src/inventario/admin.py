from django.contrib import admin
from .models import Producto, Autor, Genero, Pais, Editorial, OtrosAutores, IVA
# Register your models here.


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'isbn',
        'titulo_es', 'titulo_jp', 'precio', 'stock',
        'fecha_publicacion', 'esta_publicado', 'autor',
        'editorial'
    )


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'es_activo')


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('pais',)


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('editorial', 'pais')


@admin.register(OtrosAutores)
class OtrosAutoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cargo')
