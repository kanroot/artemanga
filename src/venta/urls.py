from django.urls import path
from .views import ConfirmarCompraView, CrearDireccionView, ElegirDireccionView, FinalizarCompraView

urlpatterns = [
    path('confirmar-compra/', ConfirmarCompraView.as_view(), name='confirmar-compra'),
    path('crear-direccion/', CrearDireccionView.as_view(), name='crear-direccion'),
    path('elegir-direccion/', ElegirDireccionView.as_view(), name='elegir-direccion'),
    path('finalizar-compra/', FinalizarCompraView.as_view(), name='finalizar-compra'),
]