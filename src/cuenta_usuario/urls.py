from django.urls import path
from .forms import UserRegisterForm, UserUpdateForm
from .views import LoginUsuario, ReinicioContrasena

urlpatterns = [

    #reset password
    path('reset-password/', ReinicioContrasena.as_view(), name='reset-password'),

    # crear
    path('crear-perfil/', UserRegisterForm.as_view(), name='crear-perfil'),

    # editar
    path('editar-perfil/<pk>/', UserUpdateForm.as_view(), name='editar-perfil'),

    #login
    path('login/', LoginUsuario.as_view(), name='login'),



]
