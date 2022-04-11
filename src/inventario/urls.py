from django.urls import re_path
from inventario import views

urlpatterns = [
    re_path('registro', views.index, name='crud_autor.html'),
    ]
