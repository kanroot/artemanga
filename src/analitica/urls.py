from django.urls import path
from.views import DetalleReporteView, ReportesListView


urlpatterns = [
    path('', ReportesListView.as_view(), name='listado-reportes'),
    path('reporte/<pk>', DetalleReporteView.as_view(), name='detalle-reporte'),
]