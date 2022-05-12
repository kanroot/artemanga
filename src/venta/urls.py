from django.urls import path
from .views import ConfirmarCompraView, CrearDireccionView, ElegirDireccionView, FinalizarCompraView, \
    ActualizarDireccionView, DireccionesView, EliminarDireccionView

urlpatterns = [
    path('confirmar-compra/', ConfirmarCompraView.as_view(), name='confirmar-compra'),
    path('elegir-direccion/', ElegirDireccionView.as_view(), name='elegir-direccion'),
    path('finalizar-compra/', FinalizarCompraView.as_view(), name='finalizar-compra'),
    path('ver-direccion/', DireccionesView.as_view(), name='ver-direccion'),
    path('crear-direccion/', CrearDireccionView.as_view(), name='crear-direccion'),
    path('editar-direccion/<int:pk>/', ActualizarDireccionView.as_view(), name='editar-direccion'),
    path('eliminar-direccion/<int:pk>/', EliminarDireccionView.as_view(), name='eliminar-direccion'),

]
