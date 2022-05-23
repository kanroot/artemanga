from django.views.generic import DetailView

from artemangaweb.mixins import VistaRestringidaMixin
from inventario.vistas_modelos.vistas_genericas import ListaGenericaView
from .models import Reporte


class ReportesListView(VistaRestringidaMixin, ListaGenericaView):
    model = Reporte
    usuarios_permitidos = VistaRestringidaMixin.todos_los_administradores
    template_name = 'administración/reportes/tabla_reportes.html'
    tabla_cabecera = ['Nombre', 'Páginas' , 'Fecha creación', 'Ver']
    context_object_name = 'reportes'
    tabla_boton_crear = None
    tabla_boton_editar = None
    tabla_boton_eliminar = None

    ordering = ['fecha_creacion']


class DetalleReporteView(VistaRestringidaMixin, DetailView):
    usuarios_permitidos = VistaRestringidaMixin.todos_los_administradores
    template_name = 'administración/reportes/detalle_reporte.html'
    model = Reporte

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        iteraciones = self.model.objects.filter(nombre=self.object.nombre)
        context['iteraciones'] = iteraciones
        return context