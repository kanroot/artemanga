from artemangaweb.exceptions import ErrorBase


class CarritoDeserializacionInvalida(ErrorBase):
    def __init__(self, diccionario: dict):
        super().__init__(CarritoDeserializacionInvalida, self).__init__(
            f"El diccionario {diccionario} no es valido para el modelo Carrito"
        )

class StockProductoInsuficiente(ErrorBase):
    def __init__(self, cantidad: int, producto: str):
        super().__init__(StockProductoInsuficiente, self).__init__(
            f"La cantidad {cantidad} excede el stock disponible para producto {producto}"
        )

class ProductoNoExiste(ErrorBase):
    def __init__(self, id_producto: int):
        super().__init__(ProductoNoExiste, self).__init__(
            f"El producto con id {id_producto} no existe en este carrito."
        )