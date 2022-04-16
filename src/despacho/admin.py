from django.contrib import admin
from .models import Despacho, Provincia, Comuna, Region, Direccion


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('id', 'calle', 'numero', 'departamento', 'piso', 'codigo_postal', 'telefono')


@admin.register(Despacho)
class DespachoAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado', 'usuario', 'direccion')
