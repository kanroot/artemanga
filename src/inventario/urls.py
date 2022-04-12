from django.urls import re_path
from inventario.views import AutorListView, GeneroListView, PaisListView, EditorialListView, OtrosAutoresListView, \
    IVAListView, ProductoListView

urlpatterns = [
    re_path('listado-producto', ProductoListView.as_view()),
    re_path('listado-autor', AutorListView.as_view()),
    re_path('listado-genero', GeneroListView.as_view()),
    re_path('listado-pais', PaisListView.as_view()),
    re_path('listado-editorial', EditorialListView.as_view()),
    re_path('listado-otro-autor', OtrosAutoresListView.as_view()),
    re_path('listado-iva', IVAListView.as_view()),
]
