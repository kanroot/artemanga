from dataclasses import dataclass
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@dataclass
class Emailer:
    asunto: str
    titulo_texto_1: str
    cuerpo_texto_1: str
    titulo_texto_2: str
    cuerpo_texto_2: str
    destinatarios: list[str]
    correo_origen: str = None
    template: str = 'emails/base.html'

    def mensaje_html(self):
        self.cuerpo_texto_1.replace('\n', '<br>')
        self.cuerpo_texto_2.replace('\n', '<br>')
        contexto = {
            'asunto': self.asunto,
            'titulo_texto_1': self.titulo_texto_1,
            'cuerpo_texto_1': self.cuerpo_texto_1,
            'titulo_texto_2': self.titulo_texto_2,
            'cuerpo_texto_2': self.cuerpo_texto_2
        }
        return render_to_string(self.template, contexto)

    def mensaje_plano(self):
        return strip_tags(self.mensaje_html())

    def enviar(self):
        send_mail(
            subject=self.asunto,
            message=self.mensaje_plano(),
            from_email=self.correo_origen,
            recipient_list=self.destinatarios,
            html_message=self.mensaje_html()
        )