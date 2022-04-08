from django.db import models
from ..catalogo.models import Oferta


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name="nombre", blank=False)
    apellido = models.CharField(max_length=200, verbose_name="apellido", blank=False)
    es_activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}"


class Genero(models.Model):
    genero = models.CharField(max_length=200, verbose_name="genero", blank=False, unique=True)


class Pais(models.Model):
    id = models.AutoField(primary_key=True)
    pais = models.CharField(max_length=200, verbose_name="pais", blank=False)


class Editorial(models.Model):
    id = models.AutoField(primary_key=True)
    editorial = models.CharField(max_length=200, verbose_name="editorial", blank=False)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, blank=False)


class OtrosAutores(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name="nombre", blank=False)
    cargo = models.CharField(max_length=200, verbose_name="cargo", blank=False)


class Producto(models.Model):
    isbn = models.CharField(max_length=200, verbose_name="isbn", blank=False, unique=True)
    titulo_es = models.CharField(max_length=200, verbose_name="titulo", blank=False)
    titulo_jp = models.CharField(max_length=200, verbose_name="titulo jp", blank=True)
    stock = models.IntegerField(verbose_name="stock", blank=False)
    portada = models.CharField(max_length=200, verbose_name="ruta de portada portada", blank=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio", blank=False)
    iva = models.IntegerField(verbose_name="iva", blank=False, default=19)
    descripcion = models.CharField(max_length=200, verbose_name="descripcion", blank=True)
    numero_paginas = models.IntegerField(verbose_name="numero de paginas", blank=False, null=False)
    es_color = models.BooleanField(default=False)
    fecha_publicacion = models.DateField(verbose_name="fecha de publicacion", blank=False, null=False)
    esta_publicado = models.BooleanField(default=False)
    es_destacado = models.BooleanField(default=False)
    # conexiones
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, blank=False)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, blank=False)
    genero = models.ManyToManyField(Genero, verbose_name="genero", blank=False)
    otros_autores = models.ForeignKey(OtrosAutores, on_delete=models.CASCADE, blank=True, null=True)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE, blank=True, null=True)
