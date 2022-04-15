import random
from datetime import date

from django.core.management.base import BaseCommand
from faker import Faker

from catalogo.models import Oferta
from inventario.models import Producto, Autor, Editorial, Genero, OtrosAutores, IVA, Pais
from tqdm import tqdm


class Command(BaseCommand):
    help = 'Inicializa la base de datos del inventario con datos de prueba.'
    fake = Faker(['es_ES', 'ja_JP'])
    cantidad: int = 100

    def add_arguments(self, parser):
        parser.add_argument('--cantidad', type=int, default=100)

    def handle(self, *args, **options):
        self.cantidad = options['cantidad']

        self.generar_generos()
        self.generar_autores()
        self.generar_otros_autores()
        self.generar_editorial()
        self.generar_IVA()
        self.generar_productos()
        self.generar_ofertas()

    def generar_IVA(self):
        print('Generando IVA...')
        iva = IVA.objects.create(iva=19)
        iva.save()

    def generar_generos(self):
        print('Generando géneros...')
        generos = [
            'Hentai', 'Acción', 'CyberPunk', 'Shonen', 'Shojo', 'Shojo-Shonen', 'Supernatural', 'Vampiros',
            'Yaoi', 'Yuri'
        ]
        for genero in generos:
            g = Genero.objects.create(nombre=genero)
            g.save()

    def generar_autores(self):
        print('Generando autores...')
        for _ in tqdm(range(self.cantidad)):
            p_nombre, apellido = self.fake.first_romanized_name(), self.fake.last_romanized_name()
            a = Autor.objects.create(nombre=p_nombre, apellido=apellido)
            a.save()

    def generar_editorial(self):
        print('Generando editoriales...')
        paises = ['Argentina', 'España', 'Chile', 'Brasil', 'Uruguay', 'Paraguay', 'Perú', 'Venezuela', 'Colombia']

        for p in paises:
            pais = Pais.objects.create(nombre=p)
            pais.save()

        for _ in tqdm(range(self.cantidad)):
            nombre = self.fake.company()
            pais = random.choice(Pais.objects.all())
            e = Editorial.objects.create(nombre=nombre, pais=pais)
            e.save()

    def generar_otros_autores(self):
        print('Generando otros autores...')
        for _ in tqdm(range(self.cantidad)):
            nombre = self.fake.name()
            cargo = self.fake['es_ES'].job()
            oa = OtrosAutores.objects.create(nombre=nombre, cargo=cargo)
            oa.save()

    def generar_productos(self):
        print('Generando productos...')

        for _ in tqdm(range(self.cantidad)):
            cant_generos = random.randint(1, 3)
            generos = [random.choice(Genero.objects.all()) for _ in range(cant_generos)]
            otros_autores = [
                random.choice(OtrosAutores.objects.all()) for _ in range(cant_generos) if
                self.fake.boolean(chance_of_getting_true=25)
            ]
            isbn = self.fake.isbn13()
            titulo_es = self.fake['es_ES'].sentence()
            titulo_jp = self.fake['ja_JP'].sentence()
            stock = random.randint(1, 100)
            precio = self.fake.pydecimal(left_digits=6, right_digits=2, positive=True)
            descripcion = self.fake['es_ES'].text()
            numero_paginas = random.randint(1, 1000)
            es_color = self.fake.boolean(chance_of_getting_true=10)
            fecha = date(*[int(d) for d in self.fake.date().split('-')])
            fecha_publicacion = fecha
            esta_publicado = self.fake.boolean()
            es_destacado = self.fake.boolean(chance_of_getting_true=10)
            autor = random.choice(Autor.objects.all())
            editorial = random.choice(Editorial.objects.all())

            iva = IVA.objects.get(iva=19)

            producto = Producto.objects.create(
                isbn=isbn, titulo_es=titulo_es, titulo_jp=titulo_jp, stock=stock, precio=precio,
                descripcion=descripcion, numero_paginas=numero_paginas, es_color=es_color,
                fecha_publicacion=fecha_publicacion, esta_publicado=esta_publicado, es_destacado=es_destacado,
                autor=autor, editorial=editorial, iva=iva
            )

            producto.save()

            for otro_autor in otros_autores:
                producto.otros_autores.add(otro_autor)
                producto.save()

            for genero in generos:
                producto.genero.add(genero)
                producto.save()

    def generar_ofertas(self):
        print('Generando ofertas...')
        productos = Producto.objects.all()
        for producto in productos:
            if not self.fake.boolean(chance_of_getting_true=10):
                continue

            descuento = random.randint(5, 90)
            fecha_inicio = self.fake.date_between(start_date='-30d', end_date='-1d')
            fecha_fin = self.fake.date_between(start_date='-1d', end_date='+30d')
            oferta = Oferta.objects.create(
                id=producto, descuento=descuento, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
            oferta.save()
