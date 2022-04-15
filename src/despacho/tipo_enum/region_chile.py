from django.db import models


class RegionChile(models.TextChoices):
    TARAPACA = '1', 'Region de Tarapacá'
    ANTOFAGASTA = '2', 'Region de Antofagasta'
    ATACAMA = '3', 'Region de Atacama'
    COQUIMBO = '4', 'Region de Coquimbo'
    VALPARAISO = '5', 'Region de Valparaíso'
    OHIGGINS = '6', 'Región del Libertador General Bernardo O’Higgins'
    MAULE = '7', 'Región del Maule'
    BIOBIO = '8', 'Región del Biobío'
    ARAUCANIA = '9', 'Región de la Araucanía'
    LAGOS = '10', 'Región de los Lagos'
    IBANEZ = '11', 'Región Aysén del General Carlos Ibáñez del Campo'
    MAGALLANES = '12', 'Región de Magallanes y de la Antártica Chilena'
    METROPOLITANA = '13', 'Región Metropolitana de Santiago'
    RIOS = '14', 'Región de los Ríos'
    ARICA_Y_PARINACOTA = '15', 'Región de Arica y Parinacota'
    NUBLE = '16', 'Región de Ñuble'
