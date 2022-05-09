from django.db import models


VALOR_IVA = 19

class Autor(models.Model):

    class Meta:
        verbose_name_plural = "Autores"

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name="nombre")
    apellido = models.CharField(max_length=200, verbose_name="apellido")
    es_activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Genero(models.Model):
    class Meta:
        verbose_name = "Género"

    nombre = models.CharField(max_length=200, verbose_name="género", unique=True)

    def __str__(self):
        return self.nombre


class Pais(models.Model):

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name="pais")

    def __str__(self):
        return self.nombre


class Editorial(models.Model):

    class Meta:
        verbose_name_plural = "Editoriales"

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name="editorial")
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class OtrosAutores(models.Model):

    class Meta:
        verbose_name_plural = "Otros Autores"

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name="nombre")
    cargo = models.CharField(max_length=200, verbose_name="cargo")

    def __str__(self):
        return f"{self.nombre}, {self.cargo}"


class Producto(models.Model):
    isbn = models.CharField(max_length=200, verbose_name="isbn", unique=True)
    titulo_es = models.CharField(max_length=200, verbose_name="titulo")
    titulo_jp = models.CharField(max_length=200, verbose_name="titulo jp", blank=True)
    stock = models.IntegerField(verbose_name="stock", blank=False)
    portada = models.ImageField(upload_to="portadas", verbose_name="portada", blank=True, default='portadas/portada.jpg')
    precio = models.IntegerField(verbose_name="precio")
    descripcion = models.CharField(max_length=200, verbose_name="descripcion", blank=True)
    numero_paginas = models.IntegerField(verbose_name="numero de paginas")
    es_color = models.BooleanField(default=False)
    fecha_publicacion = models.DateField(verbose_name="fecha de publicacion")
    esta_publicado = models.BooleanField(default=False)
    es_destacado = models.BooleanField(default=False)
    es_nuevo = models.BooleanField(default=False)
    # conexiones
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    genero = models.ManyToManyField(Genero, verbose_name="genero")
    otros_autores = models.ManyToManyField(OtrosAutores, verbose_name="otros autores", blank=True)

    def __str__(self):
        return self.titulo_es

    @property
    def precio_sin_iva(self):
        return self.precio - (self.precio * VALOR_IVA / 100)
