from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Usuario

admin.site.unregister(Group)


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'tipo_usuario', 'email', 'es_activo', 'primer_nombre', 'primer_apellido')
    fieldsets = (

        ('Información básica', {
            'classes': ('wide',),
            'fields': ('username', 'email', 'tipo_usuario', 'es_activo')
        }),
        ('Información personal', {
            'classes': ('wide',),
            'fields': ('primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'sexo')
        }),

    )
