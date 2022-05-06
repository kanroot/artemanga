from django.views.generic import TemplateView
from cuenta_usuario.restriccion import VistaRestringida
from cuenta_usuario.enums.opciones import TipoUsuario


class DashboardView(VistaRestringida, TemplateView):
    template_name = "administración/dashboard.html"
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA, TipoUsuario.VENTAS]
