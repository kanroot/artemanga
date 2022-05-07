from django.views.generic import TemplateView
from artemangaweb.mixins import VistaRestringidaMixin
from cuenta_usuario.enums.opciones import TipoUsuario


class DashboardView(VistaRestringidaMixin, TemplateView):
    template_name = "administración/dashboard.html"
    usuarios_permitidos = [TipoUsuario.ADMINISTRADOR, TipoUsuario.BODEGA, TipoUsuario.VENTAS]
