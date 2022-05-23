from django.db import models


class Reporte(models.Model):
    """Representa una interación en particular de un reporte. Por ejemplo, el 'Reporte de ventas mensual' puede tener
    más de una iteración, una por mes. Los reportes tienen páginas que contienen información de interés y un gráfico."""
    nombre = models.CharField(
        verbose_name='Nombre',
        max_length=250,
        help_text='Nombre del reporte. El reporte puede ser compartido por varias iteraciones del mismo reporte y '
                  'funciona como un identificador para agrupar los datos del mismo.',
    )
    iteracion = models.IntegerField(
        verbose_name='Iteración',
        help_text='Número de iteración del reporte. Sirve para identificar varios reportes con el mismo nombre',
        blank=True,
        default=-1
    )
    fecha_creacion = models.DateTimeField(
        verbose_name="fecha de creación",
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.nombre} #{self.iteracion}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.iteracion == -1:
            ultimo_reporte = Reporte.objects.filter(nombre=self.nombre).last()
            if not ultimo_reporte:
                self.iteracion = 1
            else:
                self.iteracion = ultimo_reporte.iteracion + 1
        super().save(force_insert, force_update, using, update_fields)

    @property
    def paginas(self):
        return Pagina.objects.filter(reporte=self)


class Pagina(models.Model):
    """Representa una página del reporte, incluye un gráfico y datos de interés."""
    titulo = models.CharField(max_length=200, verbose_name='Título')
    datos = models.JSONField(
        verbose_name='Datos',
        help_text='Datos de interés para la página. Los datos se guardan en formato JSON.'
    )
    chart_config = models.JSONField(
        verbose_name='Configuración del gráfico',
        help_text='Configuración del gráfico para la página. Los datos se guardan en formato JSON.'
    )

    # Relaciones
    reporte = models.ForeignKey(Reporte, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reporte.nombre.title()} #{self.reporte.iteracion} - Página {self.id}"
