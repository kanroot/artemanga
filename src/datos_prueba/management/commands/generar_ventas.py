import random

from django.core.management.base import BaseCommand
from venta.models import Venta, VentaProducto
from inventario.models import Producto
from despacho.models import Despacho, Direccion, Comuna
from cuenta_usuario.models import Usuario
from cuenta_usuario.enums.opciones import TipoUsuario
from faker import Faker
from tqdm import tqdm


class Command(BaseCommand):
    help = 'Genera datos de prueba para el módulo de ventas'
    fake = Faker(['es_ES'])
    cantidad: int = 0

    def add_arguments(self, parser):
        parser.add_argument('--cantidad', type=int, default=100, help='Cantidad de ventas a generar')

    def handle(self, *args, **options):
        self.cantidad = options['cantidad']
        self.generar_direcciones()
        self.generar_despachos()
        self.generar_ventas()

    def generar_direcciones(self):
        print('Creando direcciones falsas...')
        for _ in tqdm(range(self.cantidad)):
            usuario = random.choice(Usuario.objects.filter(tipo_usuario=TipoUsuario.CLIENTE.value).all())
            calle = self.fake.street_name()
            numero = self.fake.building_number()
            codigo_postal = self.fake.postcode()
            telefono = self.fake.random_int(min=1000000, max=9999999)
            comuna = random.choice(Comuna.objects.all())
            direccion = Direccion.objects.create(calle=calle, numero=numero, codigo_postal=codigo_postal,
                                                 telefono=telefono, comuna=comuna, usuario=usuario)
            direccion.save()

    def generar_despachos(self):
        print('Generando despachos...')
        for _ in tqdm(range(self.cantidad)):
            direccion = random.choice(Direccion.objects.all())
            despacho = Despacho.objects.create(
                direccion=direccion
            )
            despacho.save()

    def generar_ventas(self):
        print('Generando ventas...')
        for despacho in tqdm(Despacho.objects.all()):
            productos = []
            cant_productos = random.randint(1, 3)
            for j in range(0, cant_productos):
                p = random.choice(Producto.objects.all())
                productos.append(p)

            total = sum([p.precio for p in productos])

            venta = Venta.objects.create(
                despacho=despacho,
                total=total
            )
            venta.save()

            for p in productos:
                venta_producto = VentaProducto.objects.create(
                    venta=venta,
                    producto=p,
                    cantidad=random.randint(1, 3)
                )
                venta_producto.save()
