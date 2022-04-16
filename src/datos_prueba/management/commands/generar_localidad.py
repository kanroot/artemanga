import random
from django.core.management.base import BaseCommand
from despacho.models import Region, Provincia, Comuna, Direccion
from despacho.tipo_enum.region_chile import RegionChile
from despacho.tipo_enum.provincia_vinculada import provincias
from despacho.tipo_enum.comuna_vinculada import comunas
from faker import Faker
from tqdm import tqdm


class Command(BaseCommand):
    help = 'Genera datos de prueba para el módulo de despacho en el apartado de direcciones'
    fake = Faker(['es_ES'])

    def handle(self, *args, **options):
        self.limpiar_localidad()
        self.generar_regiones()
        self.generar_provincia()
        self.generar_comunas()
        self.generar_direccion_falsa()

    def limpiar_localidad(self):
        Provincia.objects.all().delete()
        Region.objects.all().delete()
        Comuna.objects.all().delete()
        Direccion.objects.all().delete()

    def generar_regiones(self):
        print('Creando regiones...')
        for region in tqdm(RegionChile.labels):
            r = Region.objects.create(nombre=region.upper())
            r.save()

    def generar_provincia(self):
        print('Creando provincia...')
        for prov in tqdm(provincias):
            id_region = prov[2]
            region = Region.objects.get(id=id_region)
            p = Provincia.objects.create(nombre=prov[1].upper(), region=region)
            p.save()

    def generar_comunas(self):
        print('Creando comunas...')
        for comuna in tqdm(comunas):
            id_provincia = comuna[2]
            prov = Provincia.objects.get(id=id_provincia)
            c = Comuna.objects.create(nombre=comuna[1].upper(), provincia=prov)
            c.save()

    def generar_direccion_falsa(self):
        print('Creando direcciones falsas...')
        for i in tqdm(range(1, 100)):
            calle = self.fake.street_name()
            numero = self.fake.building_number()
            codigo_postal = self.fake.postcode()
            telefono = self.fake.random_int(min=1000000, max=9999999)
            comuna = random.choice(Comuna.objects.all())
            direccion = Direccion.objects.create(calle=calle, numero=numero, codigo_postal=codigo_postal,
                                                 telefono=telefono,
                                                 comuna=comuna)
            direccion.save()
