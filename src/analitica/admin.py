from django.contrib import admin
from .models import Reporte, Pagina

class PaginaAdmin(admin.TabularInline):
    model = Pagina
    extra = 0

@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'iteracion', 'fecha_creacion')
    exclude = ('iteracion',)
    inlines = [PaginaAdmin]



