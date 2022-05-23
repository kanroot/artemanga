from .models import Dataset, Data, Config
from .excepciones import ParamConstruccionInvalido
from .utils import obtener_nuevo_color_solido, obtener_nuevo_color_transparente, TipoGrafico

def crear_config_torta(etiquetas: list[str], valores: list[int], nombre: str, **kwargs) -> str:
    if len(etiquetas) != len(valores):
        raise ParamConstruccionInvalido('Las etiquetas y los valores deben tener el mismo tamaño')

    dataset = Dataset(
        label=nombre,
        data=valores,
        backgroundColor=[next(obtener_nuevo_color_transparente) for _ in valores],
        borderColor=[next(obtener_nuevo_color_solido) for _ in valores],
    )

    data = Data(
        labels=etiquetas,
        datasets=[dataset]
    )

    config = Config(
        type=TipoGrafico.torta,
        data=data,
        options={
            'responsive': True,
            'title': {
                'display': True,
                'text': nombre
            },
            'legend': {
                'display': True,
                'position': 'bottom'
            }
        }
    )

    if kwargs.get('options'):
        config.options.update(kwargs['options'])

    return config.serializar_json()


def crear_config_barras_simple(
        categorias: list[str], eje_y: str, valores: list[int], nombre: str, **kwargs) -> str:
    return crear_config_barras_agrupadas(
        categorias=categorias,
        grupos=[eje_y],
        datos_por_grupo=[valores],
        nombre=nombre,
        **kwargs)


def crear_config_barras_agrupadas(
        categorias: list[str], grupos: list[str], datos_por_grupo: list[list[int]], nombre: str, **kwargs) -> str:
    if len(grupos) != len(datos_por_grupo):
        raise ParamConstruccionInvalido('Los grupos y los datos por grupo deben tener el mismo tamaño')

    for dato in datos_por_grupo:
        if len(categorias) != len(dato):
            raise ParamConstruccionInvalido('Los datos por grupo deben tener el mismo tamaño que las categorias')

    datasets = []

    for i in range(len(grupos)):
        dataset = Dataset(
            label=grupos[i],
            data=datos_por_grupo[i],
            backgroundColor=next(obtener_nuevo_color_transparente),
            borderColor=next(obtener_nuevo_color_solido),
            borderRadius=10
        )
        datasets.append(dataset)

    data = Data(
        labels=categorias,
        datasets=datasets
    )

    config = Config(
        type=TipoGrafico.barras,
        data=data,
        options={
            'responsive': True,
            'title': {
                'display': True,
                'text': nombre
            },
            'legend': {
                'display': True,
                'position': 'top'
            }
        }
    )

    if kwargs.get('options'):
        config.options.update(kwargs['options'])

    return config.serializar_json()

