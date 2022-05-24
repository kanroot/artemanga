from dataclasses import dataclass
from django.views.generic import DetailView
from django.views.generic import TemplateView
from artemangaweb.mixins import VistaRestringidaMixin, TituloPaginaMixin
from .models import Reporte
from django.urls import reverse

@dataclass
class ReprReporteTabla:
    nombre: str
    iteraciones: int
    url: str

    def __eq__(self, other):
        return self.nombre == other.nombre

class ReportesListView(VistaRestringidaMixin, TituloPaginaMixin, TemplateView):
    model = Reporte
    titulo_pagina = 'Reportes agrupados por nombre'
    usuarios_permitidos = VistaRestringidaMixin.todos_los_administradores
    template_name = 'administración/reportes/tabla_reportes.html'
    tabla_cabecera = ['Nombre', 'Iteraciones' , 'Ver']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tabla_cabecera'] = self.tabla_cabecera
        data = {'reportes': []}
        for reporte in Reporte.objects.all().order_by('-fecha_creacion'):
            r = ReprReporteTabla(reporte.nombre, 1, reverse('detalle-reporte', args=[reporte.pk]))
            if r in data['reportes']:
                data['reportes'][data['reportes'].index(r)].iteraciones += 1
            else:
                data['reportes'].append(r)
        context['data'] = data

        return context


class DetalleReporteView(VistaRestringidaMixin, DetailView):
    usuarios_permitidos = VistaRestringidaMixin.todos_los_administradores
    template_name = 'administración/reportes/detalle_reporte.html'
    model = Reporte

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        iteraciones = self.model.objects.filter(nombre=self.object.nombre)
        context['iteraciones'] = iteraciones
        return context