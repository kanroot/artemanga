from django.core.management.base import BaseCommand
from analitica.reportador import Reportador

class Command(BaseCommand):
    help = 'Realiza el reporte de analitica'

    def add_arguments(self, parser):
        parser.add_argument('--nombre', type=str, default='Reporte de ventas', help='Nombre del reporte')
        parser.add_argument('--fecha_inicio', type=str, default=None, help='Fecha de inicio')
        parser.add_argument('--fecha_fin', type=str, default=None, help='Fecha de fin')

    def handle(self, *args, **options):
        nombre = options['nombre']
        fecha_inicio = options['fecha_inicio']
        fecha_fin = options['fecha_fin']
        print('Realizando el reporte de analitica...')
        Reportador(fecha_inicio=fecha_inicio, fecha_fin=fecha_fin).crear_reporte_con_nombre(nombre)