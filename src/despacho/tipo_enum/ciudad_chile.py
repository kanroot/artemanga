from enum import Enum


class CiudadChile(Enum):
    PUENTE_ALTO = 'Puente Alto'
    MAIPU = 'Maipú'
    SANTIAGO = 'Santiago'
    FLORIDA = 'La Florida'
    TEMUCO = 'Temuco'
    ANTOFAGASTA = 'Antofagasta'
    VINA_DEL_MAR = 'Vina del Mar'
    SAN_BERNARDO = 'San Bernardo'
    VALPARAISO = 'Valparaíso'
    CONDES = 'Las Condes'
    PENALOLEN = 'Peñalolén'
    RANCAGUA = 'Rancagua'
    ARICA = 'Arica'
    CONCEPCION = 'Concepción'
    QUILICURA = 'Quilicura'
    NUNOA = 'ÑUÑOA'
    TALCA = 'Talca'
    PUDAHUEL = 'Pudahuel'
    SERENA = 'La Serena'
    IQUIQUE = 'Iquique'


CIUDAD_CHILE_CHOICE = [[estadoDes.value, estadoDes.name.capitalize()] for estadoDes in CiudadChile]
