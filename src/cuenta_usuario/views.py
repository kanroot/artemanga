from django.contrib.auth.views import LoginView, PasswordResetView, LogoutView
from django.views.generic import CreateView, UpdateView
from .models import Usuario
from .forms import RegistroUsuarioForm
from artemangaweb.mixins import MensajeResultadoFormMixin

class InicioSesionView(MensajeResultadoFormMixin, LoginView):
    template_name = 'login.html'
    mensaje_exito = 'Ha iniciado sesión correctamente'
    mensaje_error = 'No se ha podido iniciar sesión'
    success_url = '/'

class RegistroUsuarioView(MensajeResultadoFormMixin, CreateView):
    model = Usuario
    template_name = 'generico_form.html'
    form_class = RegistroUsuarioForm
    mensaje_exito = "Tu perfil ha sido creado con éxito"
    mensaje_error = "No se ha podido crear tu perfil"
    success_url = '/'

class ActualizarUsuarioView(MensajeResultadoFormMixin, UpdateView):
    model = Usuario
    template_name = 'generico_form.html'
    fields = ['primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'sexo']
    mensaje_exito = "Tu perfil ha sido modificado con éxito"
    mensaje_error = "No se ha podido modificar tu perfil"
    success_url = '/'

class ReinicioContrasenaView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = '/'

class CerrarSesionView(LogoutView):
    next_page = '/'

