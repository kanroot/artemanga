from django.urls import path
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.views import LoginView

urlpatterns = [

    # crear
    path('crear-perfil/', UserRegisterForm.as_view(), name='crear-perfil'),

    # editar
    path('editar-perfil/<pk>/', UserUpdateForm.as_view(), name='editar-perfil'),

    #login
    path('login/', LoginView.as_view(), name='login'),



]
