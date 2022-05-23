from enum import Enum
from itertools import cycle

class TipoGrafico(Enum):
    linea = 'line'
    barras = 'bar'
    doughnut = 'doughnut'
    torta = 'pie'
    radar = 'radar'


class ColorSolido(Enum):
    azul = 'rgb(54, 162, 235)'
    rojo = 'rgb(255, 99, 132)'
    verde = 'rgb(75, 192, 192)'
    naranja = 'rgb(255, 159, 64)'
    morado = 'rgb(153, 102, 255)'
    amarillo = 'rgb(255, 205, 86)'
    gris = 'rgb(201, 203, 207)'
    negro = 'rgb(0, 0, 0)'

    @classmethod
    def pedir(cls):
        try:
            return (color.value for color in [color for color in ColorSolido])
        except StopIteration:
            return cls.pedir()


class ColorTransparente(Enum):
    azul = 'rgba(54, 162, 235, 0.5)'
    rojo = 'rgba(255, 99, 132, 0.5)'
    verde = 'rgba(75, 192, 192, 0.5)'
    naranja = 'rgba(255, 159, 64, 0.5)'
    morado = 'rgba(153, 102, 255, 0.5)'
    amarillo = 'rgba(255, 205, 86, 0.5)'
    gris = 'rgba(201, 203, 207, 0.5)'
    negro = 'rgba(0, 0, 0, 0.5)'

    @classmethod
    def pedir(cls):
        try:
            return (color.value for color in [color for color in ColorTransparente])
        except StopIteration:
            return cls.pedir()


Color = ColorSolido | ColorTransparente
colores_solidos = [color.value for color in ColorSolido]
colores_transparentes = [color.value for color in ColorTransparente]

obtener_nuevo_color_solido = cycle(colores_solidos)
obtener_nuevo_color_transparente = cycle(colores_transparentes)