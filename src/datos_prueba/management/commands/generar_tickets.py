import random
from django.core.management.base import BaseCommand
from faker import Faker
from tqdm import tqdm
from venta.models import Venta
from contacto.models import Ticket, Mensaje
from contacto.enums.estado_ticket import ESTADO_TICKET_CHOICES
from contacto.enums.tipo_ticket import TIPO_TICKET_CHOICES


class Command(BaseCommand):
    help = 'Genera datos de prueba para el módulo de contacto'
    fake = Faker(['es_ES'])
    cantidad: int = 0

    def add_arguments(self, parser):
        parser.add_argument('--cantidad', type=int, default=100, help='Cantidad de contactos a generar')

    def handle(self, *args, **options):
        self.cantidad = options['cantidad']
        self.generar_tickets()
        self.generar_mensaje()

    def generar_tickets(self):
        print('Creando tickets falsos...')
        for _ in tqdm(range(self.cantidad)):
            venta = random.choice(Venta.objects.all())
            usuario = venta.usuario
            tipo = random.choice(TIPO_TICKET_CHOICES)[0]
            estado = random.choice(ESTADO_TICKET_CHOICES)[0]
            ticket = Ticket.objects.create(usuario=usuario, venta=venta, tipo=tipo, estado=estado)
            ticket.save()

    def generar_mensaje(self):
        print('Creando mensajes falsos...')
        for _ in tqdm(range(self.cantidad)):
            ticket = random.choice(Ticket.objects.all())
            texto = self.fake.text()
            usuario = ticket.usuario
            mensaje = Mensaje.objects.create(ticket=ticket, usuario=usuario, texto=texto)
            mensaje.save()
