from django.urls import path

from .views import (Home, VerCarritoView, ActualizarCarritoView,
                    AgregarProductoCarritoView, ProductosPorCategoriaView, ProductosPorEditorialView,
                    DetalleProducto)

urlpatterns = [
    path('', Home.as_view(), name='home'),

    # carrito
    path('ver-carrito', VerCarritoView.as_view(), name='ver-carrito'),
    path('actualizar-carrito', ActualizarCarritoView.as_view(), name='ajax-actualizar-carrito'),
    path('agregar-producto-carrito', AgregarProductoCarritoView.as_view(), name='ajax-agregar-producto-carrito'),
    path('categoria/<id>', ProductosPorCategoriaView.as_view(), name='productos-por-categoria'),
    path('editorial/<id>', ProductosPorEditorialView.as_view(), name='productos-por-editorial'),
    path('detalle-pro/<pk>',DetalleProducto.as_view(),name='detalle-producto'),
]
