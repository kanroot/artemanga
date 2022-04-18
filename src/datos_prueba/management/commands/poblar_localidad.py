from django.core.management.base import BaseCommand
from tqdm import tqdm

from datos_prueba.datos_localidad import regiones, provincias, comunas
from despacho.models import Region, Provincia, Comuna, Direccion


class Command(BaseCommand):
    help = 'Puebla la base de datos con datos de Regiones, Provincias y Comunas de Chile'

    def handle(self, *args, **options):
        self.limpiar_localidad()
        self.generar_regiones()
        self.generar_provincia()
        self.generar_comunas()

    def limpiar_localidad(self):
        Provincia.objects.all().delete()
        Region.objects.all().delete()
        Comuna.objects.all().delete()
        Direccion.objects.all().delete()

    def generar_regiones(self):
        print('Creando regiones...')
        for region in tqdm(regiones):
            r = Region.objects.create(id=region[0], nombre=region[1].upper())
            r.save()

    def generar_provincia(self):
        print('Creando provincias...')
        for prov in tqdm(provincias):
            id_region = prov[2]
            region = Region.objects.get(id=id_region)
            p = Provincia.objects.create(id=prov[0], nombre=prov[1].upper(), region=region)
            p.save()

    def generar_comunas(self):
        print('Creando comunas...')
        for comuna in tqdm(comunas):
            id_provincia = comuna[2]
            prov = Provincia.objects.get(id=id_provincia)
            c = Comuna.objects.create(id=comuna[0], nombre=comuna[1].upper(), provincia=prov)
            c.save()
