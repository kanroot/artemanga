from django.core.management import call_command
from django.core.management.base import BaseCommand
from cuenta_usuario.models import Usuario
from cuenta_usuario.enums.opciones import TipoUsuario


class Command(BaseCommand):
    help = 'Genera toda la shiet de datos prueba'
    cantidad_clientes: int | None = None
    cantidad_inventario: int | None = None
    cantidad_ventas: int | None = None
    no_admin: bool | None = None

    def add_arguments(self, parser):
        parser.add_argument('-c', '--clientes', type=int, help='Cantidad de clientes a generar')
        parser.add_argument('-i', '--inventario', type=int, help='Cantidad de productos a generar')
        parser.add_argument('-V', '--ventas', type=int, help='Cantidad de ventas a generar')
        parser.add_argument('-na', '--no-admin', action='store_true', help='No crear admin')

    def handle(self, *args, **options):
        self.manejar_argumentos(options)
        self.preparar_base_de_datos()
        self.generar_localidad()
        self.generar_admin()
        self.generar_clientes()
        self.generar_inventario()
        self.generar_ventas()
        self.generar_reportes()
        self.generar_campannas()
        self.generar_tickets()

    def preparar_base_de_datos(self):
        print('Limpiando datos en base de datos...')
        call_command('flush', interactive=False)
        print('Inicializando datos en base de datos...')
        call_command('migrate', interactive=False)

    def generar_admin(self):
        if self.no_admin:
            print('--no-admin especificado, no se creará el admin')
            return
        print('Generando admin...')
        admin = Usuario.objects.create_superuser(
            username='admin',
            email='admin@admin.com',
            password='admin',
            primer_nombre='admin',
            primer_apellido='admin',
            tipo_usuario=TipoUsuario.ADMINISTRADOR.value
        )
        ventas = Usuario.objects.create_user(
            username='ventas',
            email='ventas@admin.com',
            password='admin',
            primer_nombre='ventas',
            primer_apellido='ventas',
            tipo_usuario=TipoUsuario.VENTAS.value
        )
        bodega = Usuario.objects.create_user(
            username='bodega',
            email='bodega@admin.com',
            password='admin',
            primer_nombre='ventas',
            primer_apellido='ventas',
            tipo_usuario=TipoUsuario.BODEGA.value
        )

        admin.save()
        ventas.save()
        bodega.save()

    def generar_clientes(self):
        cliente = Usuario.objects.create_user(
            username='cliente',
            email='cliente@admin.com',
            password='admin',
            primer_nombre='ventas',
            primer_apellido='ventas',
            tipo_usuario=TipoUsuario.CLIENTE.value
        )
        cliente.save()

        if self.cantidad_clientes:
            call_command('generar_clientes', cantidad=self.cantidad_clientes)
            return
        call_command('generar_clientes')

    def generar_inventario(self):
        if self.cantidad_inventario:
            call_command('generar_inventario', cantidad=self.cantidad_inventario)
            return
        call_command('generar_inventario')

    def generar_localidad(self):
        call_command('poblar_localidad')

    def generar_ventas(self):
        if self.cantidad_ventas:
            call_command('generar_ventas', cantidad=self.cantidad_ventas)
            return
        call_command('generar_ventas')

    def generar_reportes(self):
        call_command('generar_reportes')

    def generar_campannas(self):
        call_command('generar_campannas')

    def generar_tickets(self):
        call_command('generar_tickets')

    def manejar_argumentos(self, options):
        if options.get('clientes'):
            self.cantidad_clientes = options.get('clientes')
        if options.get('inventario'):
            self.cantidad_inventario = options.get('inventario')
        if options.get('ventas'):
            self.cantidad_ventas = options.get('ventas')
        if options.get('no_admin'):
            self.no_admin = options.get('no_admin')
