from __future__ import annotations

from dataclasses import dataclass, field, asdict

from catalogo.carrito.exceptions import CarritoDeserializacionInvalida, StockProductoInsuficiente, ProductoNoExiste
from inventario.models import Producto

def validar_stock(id_producto: int, cantidad: int) -> None:
    """Valida que el stock del producto sea suficiente para la cantidad solicitada, de lo contrario lanza una
    excepción."""

    producto = Producto.objects.get(id=id_producto)
    if cantidad > producto.stock:
        raise StockProductoInsuficiente(cantidad, producto)

@dataclass
class EntradaCarrito:
    cantidad: int
    producto_id: int


@dataclass
class Carrito:
    productos: list[EntradaCarrito] = field(default_factory=list[EntradaCarrito])

    def obtener_producto(self, id_producto: int) -> EntradaCarrito:
        """Obtiene un producto del carrito a partir de su id. Si el producto no existe, se lanza una excepción."""

        for p in self.productos:
            if p.producto_id == id_producto:
                return p
        raise ProductoNoExiste(id_producto)

    def agregar_producto(self, producto: EntradaCarrito) -> None:
        """Agrega un producto al carrito. Si el producto ya existe, se aumenta la cantidad."""

        try:
            producto_existente = self.obtener_producto(producto.producto_id)
            producto_existente.cantidad += producto.cantidad
        except ProductoNoExiste:
            self.productos.append(producto)

    def eliminar_producto(self, producto_id: int) -> None:
        """Elimina un producto del carrito. Si el producto no existe, se lanza una excepción."""

        producto = self.obtener_producto(producto_id)
        self.productos.remove(producto)

    def total_producto(self, producto_id: int) -> float:
        """Calcula el total de un producto en el carrito."""

        producto = self.obtener_producto(producto_id)
        return producto.cantidad * Producto.objects.get(id=producto_id).precio

    @property
    def total(self) -> float:
        """Calcula el total del carrito."""

        total = 0
        for p in self.productos:
            total += self.total_producto(p.producto_id)
        return total

    def aumentar_cantidad_producto(self, id_producto: int, cantidad: int) -> None:
        """Aumenta la cantidad de un producto en el carrito. Si el producto no existe o excede el stock,
        se lanza una excepción"""

        producto = self.obtener_producto(id_producto)
        cantidad_final = producto.cantidad + cantidad
        validar_stock(id_producto, cantidad_final)
        producto.cantidad = cantidad_final

    def disminuir_cantidad_producto(self, id_producto: int, cantidad: int) -> None:
        """Disminuye la cantidad de un producto en el carrito. Si el producto no existe, lanza una excepción.
        Si la cantidad final es cero o menos, se elimina el producto del carrito."""

        producto = self.obtener_producto(id_producto)
        cantidad_final = producto.cantidad - cantidad
        if cantidad_final <= 0:
            self.eliminar_producto(id_producto)
            return
        producto.cantidad = cantidad_final

    def vaciar(self) -> None:
        """Vacia el carrito."""

        self.productos = []

    @staticmethod
    def cargar(session) -> Carrito:
        """Intenta crear un carrito a partir de la sesión actual. Si no existe, se crea uno nuevo."""

        if session.get('carrito', None):
            return Carrito.deserializar(session['carrito'])
        return Carrito()

    def guardar(self, session) -> None:
        """Guarda el carrito en la sesión actual."""

        session['carrito'] = self.serializar()

    def serializar(self) -> dict:
        """Serializa el carrito en un diccionario de python."""

        return asdict(self)

    @staticmethod
    def deserializar(diccionario: dict) -> Carrito:
        """Deserializa un carrito a partir de un diccionario de python y devuelve un objeto Carrito."""

        productos: list[EntradaCarrito] = []
        for p in diccionario['productos']:
            try:
                productos.append(EntradaCarrito(p['cantidad'], p['producto_id']))
            except KeyError:
                raise CarritoDeserializacionInvalida(p)

        carrito = Carrito(productos)
        return carrito

