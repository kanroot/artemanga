from django.db import models
from catalogo.models import Oferta


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name="nombre")
    apellido = models.CharField(max_length=200, verbose_name="apellido")
    es_activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}"


class Genero(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="genero", unique=True)


class Pais(models.Model):
    id = models.AutoField(primary_key=True)
    pais = models.CharField(max_length=200, verbose_name="pais")


class Editorial(models.Model):
    id = models.AutoField(primary_key=True)
    editorial = models.CharField(max_length=200, verbose_name="editorial")
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)


class OtrosAutores(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name="nombre")
    cargo = models.CharField(max_length=200, verbose_name="cargo")


class IVA(models.Model):
    iva = models.IntegerField(verbose_name="iva")


class Producto(models.Model):
    isbn = models.CharField(max_length=200, verbose_name="isbn", unique=True)
    titulo_es = models.CharField(max_length=200, verbose_name="titulo")
    titulo_jp = models.CharField(max_length=200, verbose_name="titulo jp", blank=True)
    stock = models.IntegerField(verbose_name="stock", blank=False)
    portada = models.CharField(max_length=200, verbose_name="ruta de portada portada")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="precio")
    descripcion = models.CharField(max_length=200, verbose_name="descripcion", blank=True)
    numero_paginas = models.IntegerField(verbose_name="numero de paginas")
    es_color = models.BooleanField(default=False)
    fecha_publicacion = models.DateField(verbose_name="fecha de publicacion")
    esta_publicado = models.BooleanField(default=False)
    es_destacado = models.BooleanField(default=False)
    # conexiones
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    genero = models.ManyToManyField(Genero, verbose_name="genero")
    otros_autores = models.ForeignKey(OtrosAutores, on_delete=models.CASCADE, blank=True, null=True)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE, blank=True, null=True)
    iva = models.ForeignKey(IVA, on_delete=models.CASCADE)
