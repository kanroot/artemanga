from .emailer import Emailer
from django.shortcuts import reverse

def notificar_empleado_nueva_cuenta(sender, instance, **kwargs):
    url_resest = f'https://artemanga.cl/{reverse("password_reset")}'
    asunto = '¡Bievenido a ArteMangaWeb!'
    titulo_texto_1 = asunto
    cuerpo_texto_1 = f'¡Hola {instance.nombre}!\n' \
                    f'¡Gracias por registrarte en ArteMangaWeb!\n' \
                    f'Es para nosotros un agrado tenerte trabajando con nosotros. Hemos creado tu cuenta, pero necesitamos que' \
                    f'para completar tu registro, por favor, hagas click en el siguiente enlace:\n' \
                    f'<a href={url_resest}>Restablecer contraseña</a>'
    titulo_texto_2 = 'Detalles del Usuario:'
    cuerpo_texto_2 = f'<table>' \
                    f'<tr><td><strong>Nombre</strong>:</td> <td>{instance.nombre}</td></tr>' \
                    f'<tr><td><strong>Email</strong>:</td> <td>{instance.email}</td></tr>' \
                    '</table>'

    Emailer(
        asunto=asunto,
        titulo_texto_1=titulo_texto_1,
        cuerpo_texto_1=cuerpo_texto_1,
        titulo_texto_2=titulo_texto_2,
        cuerpo_texto_2=cuerpo_texto_2,
        destinatarios=[instance.email]
    ).enviar()
