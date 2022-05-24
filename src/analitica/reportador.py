from .models import Reporte, Pagina
from dataclasses import dataclass, field
from collections import defaultdict
from venta.models import Venta, VentaProducto
from venta.enums.opciones import EstadoVenta
from .chartjs.factory import crear_config_barras_simple, crear_config_torta, crear_config_barras_agrupadas
from json import dumps
from cuenta_usuario.enums.opciones import SexoUsuario

@dataclass
class Reportador:
    fecha_inicio: str = None
    fecha_fin: str = None
    reportes: list[Reporte] = field(default_factory=list)
    reportes_por_nombre: defaultdict = field(default_factory=defaultdict)

    def __post_init__(self):
        self.reportes = Reporte.objects.all().order_by('-fecha_creacion')
        self.reportes_por_nombre = defaultdict(list)
        for reporte in self.reportes:
            self.reportes_por_nombre[reporte.nombre].append(reporte)

    def obtener_reportes_por_nombre(self, nombre: str) -> list[Reporte]:
        return self.reportes_por_nombre[nombre]

    def obtener_ultimo_reporte_por_nombre(self, nombre: str) -> Reporte:
        return self.reportes_por_nombre[nombre][-1]

    def obtener_ventas_para_reporte(self, reporte: Reporte) -> list[Venta]:
        if self.fecha_inicio and self.fecha_fin:
            # Periodo específico definido, utilizamos fechas para filtrar
            todas_las_ventas = Venta.objects.filter(
                fecha_venta__gte=self.fecha_inicio,
                fecha_venta__lt=self.fecha_fin,
                estado=EstadoVenta.APROBADA.value
            )
        elif not self.obtener_reportes_por_nombre(reporte.nombre):
            # No hay reportes previos con este nombre. Creamos uno nuevo con todos los datos
            todas_las_ventas = Venta.objects.filter(estado=EstadoVenta.APROBADA.value)
        else:
            # hay reportes previos con este nombre, considerar solo registros hasta el último reporte.
            ultimo_reporte = self.obtener_ultimo_reporte_por_nombre(reporte.nombre)
            todas_las_ventas = Venta.objects.filter(estado=EstadoVenta.APROBADA.value,
                                                    fecha_venta__gt=ultimo_reporte.fecha_creacion)

        return todas_las_ventas


    def crear_reporte_con_nombre(self, nombre: str) -> None:
        reporte = Reporte(nombre=nombre)
        todas_las_ventas = self.obtener_ventas_para_reporte(reporte)
        if not todas_las_ventas:
            print(f'No hay ventas para el reporte en el periodo {self.fecha_inicio} - {self.fecha_fin}')
            return

        pmv = self.crear_pagina_productos_mas_vendidos(reporte, todas_las_ventas)
        pgmv = self.crear_pagina_generos_mas_vendidos(reporte, todas_las_ventas)
        pgmcps = self.crear_pagina_generos_mas_consumido_por_sexo(reporte, todas_las_ventas)

        reporte.save()
        pmv.save()
        pgmv.save()
        pgmcps.save()
        print(f'Reporte {reporte} creado')

    def crear_pagina_productos_mas_vendidos(self, reporte: Reporte, ventas: list[Venta]) -> Pagina | None:
        conteo = {}

        for venta in ventas:
            for detalles in venta.detalles:
                if detalles.producto.titulo_es not in conteo.keys():
                    conteo[detalles.producto.titulo_es] = detalles.cantidad
                else:
                    conteo[detalles.producto.titulo_es] += detalles.cantidad

        datos = {
            'titulo': 'Productos más vendidos',
            'df': {
                'producto': [p for p in conteo.keys()],
                'cantidad': [c for c in conteo.values()]
            }
        }

        config = crear_config_barras_simple(
            categorias=datos['df']['producto'],
            eje_y='Cantidad',
            valores=datos['df']['cantidad'],
            nombre=datos['titulo']
        )

        productos_mas_vendidos = Pagina(reporte=reporte, titulo=datos['titulo'], datos=dumps(datos), chart_config=config)
        return productos_mas_vendidos

    def crear_pagina_generos_mas_vendidos(self, reporte: Reporte, ventas: list[Venta]) -> Pagina | None:
        conteo = {}

        for venta in ventas:
            for detalle in venta.detalles:
                for genero in detalle.producto.genero.all():
                    if genero.nombre not in conteo.keys():
                        conteo[genero.nombre] = detalle.cantidad
                    else:
                        conteo[genero.nombre] += detalle.cantidad

        datos = {
            'titulo': 'Géneros más vendidos',
            'df': {
                'genero': [g for g in conteo.keys()],
                'cantidad': [c for c in conteo.values()]
            }
        }

        config = crear_config_torta(
            etiquetas=datos['df']['genero'],
            valores=datos['df']['cantidad'],
            nombre=datos['titulo']
        )

        generos_mas_vendidos = Pagina(reporte=reporte, titulo=datos['titulo'], datos=dumps(datos), chart_config=config)
        return generos_mas_vendidos

    def crear_pagina_generos_mas_consumido_por_sexo(self, reporte: Reporte, ventas: list[Venta]) -> Pagina | None:
        df = {
            'genero': [],
            'masculino': [],
            'femenino': [],
            'otro': [],
            'no_responde': []
        }

        for venta in ventas:
            for detalle in venta.detalles:
                for genero in detalle.producto.genero.all():
                    if genero.nombre not in df['genero']:
                        df['genero'].append(genero.nombre)
                        df['masculino'].append(0)
                        df['femenino'].append(0)
                        df['otro'].append(0)
                        df['no_responde'].append(0)

                    index = df['genero'].index(genero.nombre)

                    match venta.despacho.usuario.sexo:
                        case SexoUsuario.MASCULINO.value:
                            df['masculino'][index] += detalle.cantidad
                        case SexoUsuario.FEMENINO.value:
                            df['femenino'][index] += detalle.cantidad
                        case SexoUsuario.OTRO.value:
                            df['otro'][index] += detalle.cantidad
                        case SexoUsuario.NO_RESPONDE.value:
                            df['no_responde'][index] += detalle.cantidad
                        case _:
                            df['otro'][index] += detalle.cantidad

        datos = {
            'titulo': 'Géneros más consumidos por sexo',
            'df': df
        }

        config = crear_config_barras_agrupadas(
            categorias=datos['df']['genero'],
            grupos=['Masculino', 'Femenino', 'Otro', 'No especificado'],
            datos_por_grupo=[df['masculino'], df['femenino'], df['otro'], df['no_responde']],
            nombre=datos['titulo']
        )

        generos_mas_consumidos_por_sexo = Pagina(reporte=reporte, titulo=datos['titulo'], datos=dumps(datos), chart_config=config)
        return generos_mas_consumidos_por_sexo

