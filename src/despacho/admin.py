from django.contrib import admin
from .models import Despacho


@admin.register(Despacho)
class DespachoAdmin(admin.ModelAdmin):
    list_display = ('id', 'direccion_corta', 'codigo_postal', 'usuario')
