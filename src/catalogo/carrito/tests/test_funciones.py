from django.test import TestCase

from catalogo.carrito.models import EntradaCarrito, Carrito
from catalogo.carrito.exceptions import StockProductoInsuficiente
from inventario.models import Producto
from django.core.management import call_command

class FuncionesBasicas(TestCase):
    def setUp(self) -> None:
        self.carrito = Carrito()

    def test_al_crear_carrito_esta_vacio(self):
        self.assertEqual(len(self.carrito.productos), 0)

    def test_al_agregar_producto_al_carrito_se_agrega_correctamente(self):
        entrada = EntradaCarrito(cantidad=1, pk=1)
        self.carrito.agregar_producto(entrada)

        entrada2 = EntradaCarrito(cantidad=2, pk=2)
        self.carrito.agregar_producto(entrada2)
        self.assertEqual(len(self.carrito.productos), 2)

    def test_al_eliminar_producto_del_carrito_se_elimina_correctamente(self):
        entrada = EntradaCarrito(cantidad=1, pk=1)
        self.carrito.agregar_producto(entrada)
        self.assertEqual(len(self.carrito.productos), 1)
        entrada2 = EntradaCarrito(cantidad=2, pk=2)
        self.carrito.agregar_producto(entrada2)

        self.carrito.eliminar_producto(1)
        self.assertEqual(len(self.carrito.productos), 1)

    def test_al_consultar_total_de_producto_obtiene_total(self):
        call_command('generar_inventario', cantidad=1)

        producto1 = Producto.objects.get(id=1)
        producto1.precio = 10
        producto1.save()

        entrada = EntradaCarrito(cantidad=2, pk=1)
        self.carrito.agregar_producto(entrada)
        self.assertEqual(self.carrito.total_producto(1), 20)

    def test_al_consultar_total_de_carrito_obtiene_total(self):
        call_command('generar_inventario', cantidad=2)

        producto1 = Producto.objects.get(id=1)
        producto1.precio = 10
        producto1.save()

        producto2 = Producto.objects.get(id=2)
        producto2.precio = 20
        producto2.save()

        entrada = EntradaCarrito(cantidad=2, pk=1)
        self.carrito.agregar_producto(entrada)
        entrada2 = EntradaCarrito(cantidad=2, pk=2)
        self.carrito.agregar_producto(entrada2)
        self.assertEqual(self.carrito.total, 60)

    def test_al_aumentar_cantidad_de_producto_aumenta(self):
        call_command('generar_inventario', cantidad=1)
        producto = Producto.objects.get(id=1)
        producto.stock = 10
        producto.save()

        entrada = EntradaCarrito(cantidad=1, pk=1)
        self.carrito.agregar_producto(entrada)
        self.carrito.aumentar_cantidad_producto(1, 1)
        esperado = {
            'productos': [
                        {'cantidad': 2, 'pk': 1}
            ]
        }

        self.assertEqual(esperado, self.carrito.serializar())

    def test_disminuir_cantidad_de_producto_disminuye(self):
        entrada = EntradaCarrito(cantidad=1, pk=1)
        self.carrito.agregar_producto(entrada)
        entrada2 = EntradaCarrito(cantidad=2, pk=2)
        self.carrito.agregar_producto(entrada2)
        self.carrito.disminuir_cantidad_producto(2, 1)

        esperado = {
            'productos': [
                {'cantidad': 1, 'pk': 1},
                {'cantidad': 1, 'pk': 2}
            ]
        }

        self.assertEqual(esperado, self.carrito.serializar())

    def test_al_aumentar_cantidad_mayor_a_stock_levanta_excepcion(self):
        call_command('generar_inventario', cantidad=1)
        producto = Producto.objects.get(id=1)
        producto.stock = 10
        producto.save()

        entrada = EntradaCarrito(cantidad=10, pk=1)
        self.carrito.agregar_producto(entrada)
        with self.assertRaises(StockProductoInsuficiente):
            self.carrito.aumentar_cantidad_producto(1, 1)

    def test_al_agregar_mismo_producto_aumenta_cantidad(self):
        entrada = EntradaCarrito(cantidad=1, pk=1)
        self.carrito.agregar_producto(entrada)
        entrada2 = EntradaCarrito(cantidad=2, pk=1)
        self.carrito.agregar_producto(entrada2)

        esperado = {
            'productos': [
                {'cantidad': 3, 'pk': 1}
            ]
        }

        self.assertEqual(esperado, self.carrito.serializar())

    def test_al_reducir_cantidad_a_cero_producto_se_elimina(self):
        entrada = EntradaCarrito(cantidad=1, pk=1)
        self.carrito.agregar_producto(entrada)
        self.carrito.disminuir_cantidad_producto(1, 1)
        esperado = {
            'productos': []
        }

        self.assertEqual(esperado, self.carrito.serializar())

