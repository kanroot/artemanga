from django.contrib import admin
from .models import Venta, VentaProducto


class VentaProductoInline(admin.TabularInline):
    model = VentaProducto
    extra = 0

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_venta', 'total', 'estado')
    inlines = [VentaProductoInline]