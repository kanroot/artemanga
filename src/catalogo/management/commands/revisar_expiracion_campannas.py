from datetime import datetime

from django.core.management.base import BaseCommand
from catalogo.models import Campanna, EstadoCampanna

class Command(BaseCommand):
    help = 'Inspecciona las campañas y cambia el estado de las que ya estén expiradas'

    def handle(self, *args, **options):
        print('Revisando campañas...')

        campannas = Campanna.objects.filter(estado=EstadoCampanna.PUBLICADA.value)
        for campanna in campannas:
            if campanna.fecha_expiracion < datetime.now():
                campanna.estado = EstadoCampanna.INACTIVA.value
                campanna.save()