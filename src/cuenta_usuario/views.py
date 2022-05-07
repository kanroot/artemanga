from django.contrib.auth.views import LoginView, PasswordResetView, LogoutView
from django.http import Http404
from django.views.generic import CreateView, UpdateView
from .models import Usuario
from .forms import RegistroUsuarioForm
from artemangaweb.mixins import MensajeResultadoFormMixin, VistaRestringidaMixin
from .enums.opciones import TipoUsuario


class InicioSesionView(MensajeResultadoFormMixin, LoginView):
    template_name = 'web/login.html'
    mensaje_exito = 'Ha iniciado sesión correctamente'
    mensaje_error = ''
    success_url = '/'


class RegistroUsuarioView(MensajeResultadoFormMixin, CreateView):
    model = Usuario
    template_name = 'web/generico_form.html'
    form_class = RegistroUsuarioForm
    mensaje_exito = "Tu perfil ha sido creado con éxito"
    mensaje_error = "No se ha podido crear tu perfil"
    success_url = '/'


class ActualizarUsuarioView(VistaRestringidaMixin, MensajeResultadoFormMixin, UpdateView):
    usuarios_permitidos = [TipoUsuario.CLIENTE]
    model = Usuario

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        queryset = queryset.filter(pk=self.request.user.pk)
        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("No user matching this query")
        return obj

    template_name = 'web/generico_form.html'
    fields = ['primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'sexo']
    mensaje_exito = "Tu perfil ha sido modificado con éxito"
    mensaje_error = "No se ha podido modificar tu perfil"
    success_url = '/'


class ReinicioContrasenaView(MensajeResultadoFormMixin, PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    mensaje_exito = "Te hemos enviado un correo con las instrucciones para reiniciar tu contraseña"
    mensaje_error = "No se ha podido enviar el correo"


class CerrarSesionView(LogoutView):
    next_page = '/'
