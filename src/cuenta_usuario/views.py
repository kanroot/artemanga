from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordResetView


class LoginUsuario(LoginView):
    template_name = 'login.html'


class ReinicioContrasena(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'

