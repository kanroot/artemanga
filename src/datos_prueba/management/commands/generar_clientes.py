from django.core.management.base import BaseCommand
from faker import Faker
from cuenta_usuario.models import Usuario
from tqdm import tqdm


class Command(BaseCommand):
    help = 'Genera una cantidad de clientes de prueba'
    fake = Faker(['es_ES'])

    def add_arguments(self, parser):
        parser.add_argument('--cantidad', type=int, default=100)

    def handle(self, *args, **options):
        print(f'Generando {options.get("cantidad")} clientes...')
        for _ in tqdm(range(options.get('cantidad'))):
            self.generar_cliente()

        print(f'generados {Usuario.objects.count()} clientes')

    def generar_cliente(self):
        primer_nombre = self.fake.first_name()
        primer_apellido = self.fake.last_name()
        segundo_apellido = self.fake.last_name()
        username = self.fake.user_name()
        email = self.fake.email()
        usuario = Usuario.objects.create(
            primer_nombre=primer_nombre,
            primer_apellido=primer_apellido,
            segundo_apellido=segundo_apellido,
            username=username,
            email=email,
        )
        usuario.save()
        if self.fake.boolean(chance_of_getting_true=10):
            usuario.segundo_nombre = self.fake.first_name()
            usuario.save()
        password = self.fake.password()
        usuario.set_password(password)
