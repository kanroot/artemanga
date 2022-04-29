from django.contrib.auth.models import AbstractUser
from django.db import models
from .enums.opciones import TipoUsuario, TIPO_CHOICES, SexoUsuario, SEXO_CHOICES
from .validators import UsernameValidator


class Usuario(AbstractUser):
    class Meta:
        verbose_name_plural = "Usuarios"

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, validators=[UsernameValidator()])
    primer_nombre = models.CharField(max_length=200, verbose_name="primer nombre", db_index=True)
    segundo_nombre = models.CharField(max_length=200, verbose_name="segundo nombre", blank=True)
    primer_apellido = models.CharField(max_length=200, verbose_name="primer apellido", db_index=True)
    segundo_apellido = models.CharField(max_length=200, verbose_name="segundo apellido", blank=True)
    es_activo = models.BooleanField(default=True)
    sexo = models.PositiveSmallIntegerField(choices=SEXO_CHOICES, default=SexoUsuario.NO_RESPONDE.value)
    tipo_usuario = models.PositiveSmallIntegerField(choices=TIPO_CHOICES, default=TipoUsuario.CLIENTE.value)

    REQUIRED_FIELDS = ['primer_nombre', 'primer_apellido']

    def __str__(self):
        return f"{self.username}"

    def es_ventas(self) -> bool:
        return self.tipo_usuario == TipoUsuario.VENTAS.value

    def es_bodega(self) -> bool:
        return self.tipo_usuario == TipoUsuario.BODEGA.value

    def es_sysadmin(self) -> bool:
        return self.tipo_usuario == TipoUsuario.ADMINISTRADOR.value

    def es_cliente(self) -> bool:
        return self.tipo_usuario <= TipoUsuario.CLIENTE.value

    def generar_pass_temporal_empleados(self) -> str:
        ident = f"{str(self.id).zfill(2)[:2]}"
        primer_nombre = f"{self.primer_nombre.upper()[:2]}"
        primer_apellido = f"{self.primer_apellido.lower()[-2:]}"
        fecha_registro = f"{self.date_joined[-2:]}"
        return f"{ident}{primer_nombre}{primer_apellido}{fecha_registro}"
