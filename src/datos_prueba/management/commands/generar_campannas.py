from django.core.management.base import BaseCommand
from catalogo.models import Campanna, EstadoCampanna, RedirigeA

class Command(BaseCommand):
    help = 'Genera 3 campañas de prueba usando las fotos de los perritos'

    def handle(self, *args, **options):
        print('Generando campañas...')

        campanna1 = Campanna(
            nombre='Campanna 1',
            estado=EstadoCampanna.PUBLICADA.value,
            imagen='campañas/template.png',
            redirige_a=RedirigeA.GENERO.value,
            key_url='1'
        )
        campanna1.save()

        campanna2 = Campanna(
            nombre='Campanna 2',
            estado=EstadoCampanna.PUBLICADA.value,
            imagen='campañas/template1.png',
            redirige_a=RedirigeA.PRODUCTO.value,
            key_url='1'
        )
        campanna2.save()

        campanna3 = Campanna(
            nombre='Campanna 3',
            estado=EstadoCampanna.PUBLICADA.value,
            imagen='campañas/template2.png',
            redirige_a=RedirigeA.EDITORIAL.value,
            key_url='1'
        )
        campanna3.save()