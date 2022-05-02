from django.urls import path
from .views import InicioSesionView, ReinicioContrasenaView, RegistroUsuarioView, CerrarSesionView, \
    ActualizarUsuarioView

urlpatterns = [
    path('reset-password/', ReinicioContrasenaView.as_view(), name='reset-password'),
    path('crear-perfil/', RegistroUsuarioView.as_view(), name='crear-perfil'),
    path('editar-perfil/', ActualizarUsuarioView.as_view(), name='editar-perfil'),
    path('login/', InicioSesionView.as_view(), name='login'),
    path('logout/', CerrarSesionView.as_view(), name='logout'),
]
