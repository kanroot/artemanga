from django.urls import path
from .views import SignUpView

urlpatterns = [

    # crear
    path('crear-perfil/', SignUpView.as_view(), name='crear-perfil'),

    # editar
    #path('editar-perfil/<pk>/', ModifyProfileView.as_view(), name='editar-perfil'),

    # eliminar
    #path('eliminar-perfil/<pk>/', DeleteProfileView.as_view(), name='eliminar-perfil'),

]
