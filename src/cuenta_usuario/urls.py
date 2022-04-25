from django.urls import path
from .forms import UserRegisterForm, UserUpdateForm
from .views import LoginUsuario

urlpatterns = [

    # crear
    path('crear-perfil/', UserRegisterForm.as_view(), name='crear-perfil'),

    # editar
    path('editar-perfil/<pk>/', UserUpdateForm.as_view(), name='editar-perfil'),

    #login
    path('login/', LoginUsuario.as_view(), name='login'),



]
