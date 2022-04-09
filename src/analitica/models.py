from django.db import models


class Reporte(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(verbose_name="fecha de creacion")
    reporte = models.JSONField(verbose_name="reporte", blank=False)
