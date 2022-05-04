from django.test import TestCase

from catalogo.carrito.exceptions import CarritoDeserializacionInvalida
from catalogo.carrito.models import Carrito, EntradaCarrito


class Serializacion(TestCase):
    def setUp(self) -> None:
        self.carrito = Carrito()
        self.session = {}

    def test_al_serializar_carrito_obtiene_diccionario (self):
        entrada = EntradaCarrito(cantidad=1, pk=1)
        self.carrito.agregar_producto(entrada)
        resultado = self.carrito.serializar()
        esperado = {'productos': [
            {'cantidad': 1, 'pk': 1}
        ]}
        self.assertEqual(esperado, resultado)

        entrada2 = EntradaCarrito(cantidad=2, pk=2)
        self.carrito.agregar_producto(entrada2)
        resultado = self.carrito.serializar()
        esperado = {'productos': [
            {'cantidad': 1, 'pk': 1},
            {'cantidad': 2, 'pk': 2}
        ]}
        self.assertEqual(esperado, resultado)

        self.carrito.eliminar_producto(1)
        resultado = self.carrito.serializar()
        esperado = {'productos': [
            {'cantidad': 2, 'pk': 2}
        ]}
        self.assertEqual(esperado, resultado)

    def test_al_deserializar_obtiene_carrito(self):
        dicc = {
            'productos': [
                {'cantidad': 1, 'pk': 1},
                {'cantidad': 2, 'pk': 2}
            ]
        }

        carrito = Carrito.deserializar(dicc)
        self.assertEqual(len(carrito.productos), 2)
        self.assertEqual(carrito.productos[0].cantidad, 1)
        self.assertEqual(carrito.productos[0].pk, 1)
        self.assertEqual(dicc, carrito.serializar())

    def test_al_deserializar_con_dicc_invalido_levanta_excepcion(self):
        dicc = {
            'productos': [
                {'c': 1, 'producto_id': 1},
                {'c': 2, 'producto_id': 2}
            ]
        }

        with self.assertRaises(CarritoDeserializacionInvalida):
            Carrito.deserializar(dicc)

    def test_al_cargar_carrito_deseraliza_desde_sesion(self):
        self.session['carrito'] = {
            'productos': [
                {'cantidad': 1, 'pk': 1},
                {'cantidad': 2, 'pk': 2}
            ]
        }

        carrito = Carrito.cargar(self.session)
        self.assertEqual(len(carrito.productos), 2)
        self.assertEqual(self.session['carrito'], carrito.serializar())

    def test_al_guardar_carrito_serializa_a_sesion(self):
        entrada1 = EntradaCarrito(cantidad=1, pk=1)
        self.carrito.agregar_producto(entrada1)
        entrada2 = EntradaCarrito(cantidad=2, pk=2)
        self.carrito.agregar_producto(entrada2)
        self.carrito.guardar(self.session)
