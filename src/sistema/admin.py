from django.contrib import admin
from .models import RegistroError

@admin.register(RegistroError)
class RegistroErrorAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'data', 'error', 'descripcion', 'pagina', 'usuario')
