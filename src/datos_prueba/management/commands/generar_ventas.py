import random

from django.core.management.base import BaseCommand
from venta.models import Venta
from inventario.models import Producto
from despacho.models import Despacho
from cuenta_usuario.models import Usuario
from cuenta_usuario.tipo_enum.tipo_usuario import Tipo
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
        self.generar_despachos()
        self.generar_ventas()

    def generar_despachos(self):
        print('Generando despachos...')
        for _ in tqdm(range(self.cantidad)):
            usuario = random.choice(Usuario.objects.filter(tipo_usuario=Tipo.CLIENTE.value).all())
            despacho = Despacho.objects.create(
                usuario=usuario
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
                venta.productos.add(p)
            venta.save()
