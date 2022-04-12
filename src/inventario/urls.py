from django.urls import re_path
from inventario import views
from .views import ProductoList
from inventario.views import AutorListView, GeneroListView, PaisListView, EditorialListView, OtrosAutoresListView, \
    IVAListView, ProductoListView

urlpatterns = [
    re_path('listado-productos', ProductoList.as_view(), name='listado'),
    re_path('crud-autor', AutorListView.as_view()),
    re_path('crud-genero', GeneroListView.as_view()),
    re_path('crud-pais', PaisListView.as_view()),
    re_path('crud-editorial', EditorialListView.as_view()),
    re_path('crud-otros-autores', OtrosAutoresListView.as_view()),
    re_path('crud-iva', IVAListView.as_view()),
    re_path('crud-producto', ProductoListView.as_view()),
]
