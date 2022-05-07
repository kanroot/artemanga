from django.db import models
from cuenta_usuario.models import Usuario

class RegistroError(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    error = models.CharField(max_length=512)
    descripcion = models.CharField(max_length=512)
    data = models.JSONField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    pagina = models.CharField(max_length=512, null=True, blank=True)
