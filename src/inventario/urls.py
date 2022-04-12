from django.urls import re_path
from inventario import views
from .views import ProductoList

urlpatterns = [
    re_path('crud-autor', views.crud_autor, name='listado.html'),
    re_path('crud-genero', views.crud_genero, name='listado.html'),
    re_path('crud-pais', views.crud_pais, name='listado.html'),
    re_path('crud-editorial', views.crud_editorial, name='listado.html'),
    re_path('crud-otros-autores', views.crud_otros_autores, name='listado.html'),
    re_path('crud-iva', views.crud_iva, name='listado.html'),
    re_path('crud-producto', views.crud_producto, name='listado.html'),
    re_path('listado-productos', ProductoList.as_view(), name='listado'),
]
