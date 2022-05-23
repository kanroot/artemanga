from dataclasses import dataclass, asdict
from .utils import TipoGrafico, Color
from json import dumps

@dataclass
class Dataset:
    label: str
    data: list
    borderColor: list[Color]
    backgroundColor: list[Color]
    borderWidth: int = 2
    borderRadius: int = 0
    borderSkipped: bool = False


@dataclass
class Data:
    labels: list[str]
    datasets: list[Dataset]


@dataclass
class Config:
    type: TipoGrafico
    data: Data
    options: dict

    def serializar_json(self):
        diccionario = self.serializar_dict()
        diccionario['type'] = diccionario['type'].value
        return dumps(diccionario)

    def serializar_dict(self):
        return asdict(self)