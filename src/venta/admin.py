from django.contrib import admin
from .models import Venta, VentaProducto, Region, Provincia, Comuna, Direccion, Despacho, ComprobanteTemporal


class VentaProductoInline(admin.TabularInline):
    model = VentaProducto
    extra = 0

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_venta', 'total', 'estado')
    inlines = [VentaProductoInline]


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
    list_display = ('id', 'usuario', 'calle', 'numero', 'departamento', 'piso', 'codigo_postal', 'telefono', 'comuna', 'provincia', 'region')


@admin.register(Despacho)
class DespachoAdmin(admin.ModelAdmin):
    list_display = ('id', 'estado', 'usuario', 'direccion')


@admin.register(ComprobanteTemporal)
class ComprobanteTemporalAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'fecha_creacion')
