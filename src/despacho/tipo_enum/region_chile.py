from enum import Enum


class RegionChile(Enum):
    TARAPACA = 'Region de Tarapacá'
    ANTOFAGASTA = 'Region de Antofagasta'
    ATACAMA = 'Region de Atacama'
    COQUIMBO = 'Region de Coquimbo'
    VALPARAISO = 'Region de Valparaíso'
    OHIGGINS = 'Región del Libertador General Bernardo O’Higgins'
    MAULE = 'Región del Maule'
    BIOBIO = 'Región del Biobío'
    ARAUCANIA = 'Región de la Araucanía'
    LAGOS = 'Región de los Lagos'
    IBANEZ = 'Región Aysén del General Carlos Ibáñez del Campo'
    MAGALLANES = 'Región de Magallanes y de la Antártica Chilena'
    METROPOLITANA = 'Región Metropolitana de Santiago'
    RIOS = 'Región de los Ríos'
    ARICA_Y_PARINACOTA = 'Región de Arica y Parinacota'
    NUBLE = 'Región de Ñuble'


REGION_CHILE_CHOISE = [[regionDes.value, regionDes.name.capitalize()] for regionDes in RegionChile]
