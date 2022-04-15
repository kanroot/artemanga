from django.contrib import admin
from .models import Oferta


@admin.register(Oferta)
class OfertaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descuento', 'fecha_inicio', 'fecha_fin', 'es_valida')
