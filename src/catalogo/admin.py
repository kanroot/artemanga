from django.contrib import admin

from .models import Oferta, Campanna


@admin.register(Oferta)
class OfertaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descuento', 'fecha_inicio', 'fecha_fin')
    list_filter = ('id', 'fecha_inicio', 'fecha_fin')


@admin.register(Campanna)
class CampannaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'estado',
        'auto_expira',
        'fecha_expiracion',
        'redirige_a',
        'key_url',
        'imagen',
    )
    list_filter = ('auto_expira', 'fecha_expiracion')