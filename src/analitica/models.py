from django.db import models


class Reportes(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(verbose_name="fecha de creacion", blank=False, null=False)
    reporte = models.JSONField(verbose_name="reporte", blank=False)
