import datetime

from django.core.validators import URLValidator, ValidationError
from django.db import models
from django.shortcuts import reverse

from inventario.models import Producto, Genero, Editorial
from .enums.opciones import ESTADO_CAMPANNA_CHOICES, REDIRIGEA_CHOICES, EstadoCampanna, RedirigeA


class Oferta(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    descuento = models.IntegerField(verbose_name="descuento", default=10)
    fecha_inicio = models.DateField(verbose_name="fecha inicio")
    fecha_fin = models.DateField(verbose_name="fecha fin")

    def __str__(self):
        return f"Oferta {'activa' if self.es_valida else 'inactiva'} " \
               f"para {self.producto.titulo_es} por {self.descuento}% de descuento"

    @property
    def es_valida(self):
        fecha_actual = datetime.date.today()
        return (self.fecha_inicio <= fecha_actual) and (fecha_actual <= self.fecha_fin)


class Campanna(models.Model):
    """Representa una campaña que será destacada en el banner de la página principal"""

    nombre = models.CharField(
        max_length=100,
        verbose_name='Nombre',
        help_text='Nombre de la campaña. Útil para encontrarla más fácilmente en el menú de administración.')

    estado = models.PositiveIntegerField(
        verbose_name='Estado',
        choices=ESTADO_CAMPANNA_CHOICES,
        default=EstadoCampanna.DRAFT.value,
        help_text='Estado de una campaña. Determina su visibilidad en el banner de la página principal')

    auto_expira = models.BooleanField(
        verbose_name='Auto expira',
        default=False,
        help_text='Si se activa, la campaña se expira automáticamente cuando la fecha de expiración se haya alcanzado.')

    fecha_expiracion = models.DateField(
        verbose_name='Fecha expiración',
        help_text='Si auto expiración está activa, la campaña pasará a inactiva una vez alcanzada esta fecha, '
                  'de otro modo no tiene efecto.',
        default=datetime.date.today() + datetime.timedelta(days=30)
    )

    redirige_a = models.PositiveIntegerField(
        verbose_name='Redirige a',
        choices=REDIRIGEA_CHOICES,
        default=RedirigeA.PRODUCTO.value,
        help_text='Determina a qué se redirige al hacer click en la campaña. La forma en que se resuelva la URL '
                  'dependerá de este campo.')

    key_url = models.CharField(
        max_length=100,
        verbose_name='Llave URL',
        help_text='Dependiendo del tipo de redirección, esta llave puede ser una ID de un objeto de la base de datos '
                  'o una URL entera en caso de elegir "OTRO".')

    imagen = models.ImageField(
        verbose_name='Imagen',
        upload_to='campañas',
        help_text='Imagen que se mostrará en el banner de la página principal.')

    @property
    def url_resuelta(self):
        match self.redirige_a:
            case RedirigeA.PRODUCTO.value:
                return reverse('detalle-producto', args=[self.key_url])
            case RedirigeA.GENERO.value:
                return reverse('productos-por-categoria', args=[self.key_url])
            case RedirigeA.AUTOR.value:
                return NotImplemented('La búsqueda de productos por autor no ha sido implementada.')
            case RedirigeA.EDITORIAL.value:
                return reverse('productos-por-editorial', args=[self.key_url])
            case RedirigeA.OTRO.value:
                # en caso de otro, se devuelve la key tal cual
                return self.key_url
            case _:
                raise ValueError('El valor de redirige_a no es válido.')

    @property
    def estado_humanizado(self):
        return EstadoCampanna(self.estado).name

    @property
    def redireccion_humanizada(self):
        tipo = f'{RedirigeA(self.redirige_a).name}'
        match self.redirige_a:
            case RedirigeA.PRODUCTO.value:
                return f'{tipo}: {Producto.objects.get(pk=self.key_url)}'
            case RedirigeA.GENERO.value:
                return f'{tipo}: {Genero.objects.get(pk=self.key_url)}'
            case RedirigeA.AUTOR.value:
                return NotImplemented('La búsqueda de productos por autor no ha sido implementada.')
            case RedirigeA.EDITORIAL.value:
                return f'{tipo}: {Editorial.objects.get(pk=self.key_url)}'
            case _:
                return f'{tipo}: {self.key_url}'

    def clean(self):
        match self.redirige_a:
            case RedirigeA.PRODUCTO.value:
                try:
                    Producto.objects.get(pk=self.key_url)
                except Producto.DoesNotExist:
                    raise ValidationError({'key_url': f'No existe un producto con ID: {self.key_url}.'})
            case RedirigeA.GENERO.value:
                try:
                    Genero.objects.get(id=self.key_url)
                except Genero.DoesNotExist:
                    raise ValidationError({'key_url': f'No existe un género con ID: {self.key_url}.'})
            case RedirigeA.AUTOR.value:
                raise ValidationError({'key_url': f'La búsqueda de productos por autor no ha sido implementada.'})
            case RedirigeA.EDITORIAL.value:
                try:
                    Editorial.objects.get(id=self.key_url)
                except Editorial.DoesNotExist:
                    raise ValidationError({'key_url': f'No existe una editorial con ID: {self.key_url}'})
            case RedirigeA.OTRO.value:
                validator = URLValidator()
                try:
                    validator(self.key_url)
                except ValidationError:
                    raise ValidationError({'key_url': f'La URL: {self.key_url} no parece ser válida.'})
            case _:
                raise ValidationError({'redirige_a': f'El tipo de redirección: {self.redirige_a} no es válido.'})
