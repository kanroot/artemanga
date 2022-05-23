from dateutil.relativedelta import relativedelta
from django.core.management.base import BaseCommand
from venta.models import Venta
from django.core.management import call_command
from datetime import datetime, date

class Command(BaseCommand):
    help = 'Genera los reportes utilizando las ventas de prueba como fuente de datos'

    def handle(self, *args, **options):
        print('Generando reportes...')
        primera_fecha = Venta.objects.all().order_by('fecha_venta').first().fecha_venta
        ultima_fecha = Venta.objects.all().order_by('-fecha_venta').first().fecha_venta
        ultima_fecha = self.get_ultima_fecha_del_mes(ultima_fecha)

        cursor_fecha = datetime(primera_fecha.year, primera_fecha.month, 1)
        while cursor_fecha <= ultima_fecha:
            print(f'Generando reporte para mes {cursor_fecha.month} de año {cursor_fecha.year}')
            fec_inicial = cursor_fecha
            fec_final = cursor_fecha + relativedelta(months=1)
            call_command('realizar_reporte_ventas', nombre='Reporte ventas mensual', fecha_inicio=fec_inicial, fecha_fin=fec_final)
            cursor_fecha += relativedelta(months=1)

        # generar reporte del año
        call_command(
            'realizar_reporte_ventas',
            nombre=f'Reporte ventas anual {primera_fecha.year}',
            fecha_inicio=datetime(primera_fecha.year, 1, 1),
            fecha_fin=datetime(primera_fecha.year, 12, 31))

    def get_ultima_fecha_del_mes(self, fecha: date) -> date:
        return datetime(fecha.year, fecha.month, 1) + relativedelta(months=1, days=-1)






