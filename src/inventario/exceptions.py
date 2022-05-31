from artemangaweb.exceptions import ErrorBase


class PrecioConOfertasMenorACero(ErrorBase):
    def __init__(self, producto: str, precio: int):
        super().__init__(f"El precio de oferta del producto {producto} es menor a cero: {precio}")
