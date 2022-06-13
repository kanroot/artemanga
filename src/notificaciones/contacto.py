from .emailer import Emailer


def notificar_nuevo_ticket(sender, instance, **kwargs):
    def enviar_correo_cliente():
        asunto = 'Nuevo Ticket'
        titulo_texto_1 = asunto
        cuerpo_texto_1 = f'El ticket {instance.id} ha sido creado'
        titulo_texto_2 = 'Detalles del Ticket:'
        cuerpo_texto_2 = f'<table>' \
                        f'<tr><td><strong>Título</strong>:</td> <td>{instance.titulo}</td></tr>' \
                        f'<tr><td><strong>Tipo</strong>:</td> <td>{instance.tipo}</td></tr>' \
                        f'<tr><td><strong>Estado</strong>:</td> <td>{instance.estado_humanizado}</td></tr>' \
                        f'<tr><td><strong>Fecha de creación</strong>:</td> <td>{instance.fecha_creacion}</td></tr>' \
                        '</table>'
        Emailer(
            asunto=asunto,
            titulo_texto_1=titulo_texto_1,
            cuerpo_texto_1=cuerpo_texto_1,
            titulo_texto_2=titulo_texto_2,
            cuerpo_texto_2=cuerpo_texto_2,
            destinatarios=[instance.usuario.email]
        ).enviar()

    def enviar_correo_admin():
        from cuenta_usuario.enums.opciones import TipoUsuario
        from cuenta_usuario.models import Usuario

        asunto = 'Nuevo Ticket'
        titulo_texto_1 = asunto
        cuerpo_texto_1 = f'Hay un nuevo ticket en el portal de soporte!'
        titulo_texto_2 = 'Detalles del Ticket:'
        cuerpo_texto_2 = f'<table>' \
                        f'<tr><td><strong>Título</strong>:</td> <td>{instance.titulo}</td></tr>' \
                        f'<tr><td><strong>Usuario</strong>:</td> <td>{instance.usuario}</td></tr>' \
                        f'<tr><td><strong>Tipo</strong>:</td> <td>{instance.tipo}</td></tr>' \
                        f'<tr><td><strong>Estado</strong>:</td> <td>{instance.estado_humanizado}</td></tr>' \
                        f'<tr><td><strong>Fecha de creación</strong>:</td> <td>{instance.fecha_creacion}</td></tr>' \
                        '</table>'
        admins = Usuario.objects.filter(tipo=TipoUsuario.VENTAS)
        Emailer(
            asunto=asunto,
            titulo_texto_1=titulo_texto_1,
            cuerpo_texto_1=cuerpo_texto_1,
            titulo_texto_2=titulo_texto_2,
            cuerpo_texto_2=cuerpo_texto_2,
            destinatarios=[admin.email for admin in admins]
        ).enviar()

    enviar_correo_cliente()
    enviar_correo_admin()


def notificar_cliente_respuesta_admin(sender, instance, **kwargs):
    asunto = f'Respuesta a tu ticket #{instance.ticket.id} - {instance.ticket.titulo}'
    titulo_texto_1 = asunto
    cuerpo_texto_1 = f'Hay una nueva respuesta a tu ticket, por favor ingresa a nuestro portal de soporte y revísala.'
    titulo_texto_2 = 'Detalles de la respuesta:'
    cuerpo_texto_2 = f'<table>' \
                    f'<tr><td><strong>Título</strong>:</td> <td>{instance.ticket.titulo}</td></tr>' \
                    f'<tr><td><strong>Tipo</strong>:</td> <td>{instance.ticket.tipo}</td></tr>' \
                    f'<tr><td><strong>Mensaje</strong>:</td> <td>{instance.texto}</td></tr>' \
                    f'<tr><td><strong>Fecha de creación</strong>:</td> <td>{instance.fecha_creacion}</td></tr>' \
                    '</table>'
    Emailer(
        asunto=asunto,
        titulo_texto_1=titulo_texto_1,
        cuerpo_texto_1=cuerpo_texto_1,
        titulo_texto_2=titulo_texto_2,
        cuerpo_texto_2=cuerpo_texto_2,
        destinatarios=[instance.ticket.usuario.email]
    ).enviar()


def notificar_admin_respuesta_cliente(sender, instance, **kwargs):
    asunto = f'Respuesta al ticket #{instance.ticket.id} - {instance.ticket.titulo}'
    titulo_texto_1 = asunto
    cuerpo_texto_1 = f'El cliente ha respondido su ticket.'
    titulo_texto_2 = 'Detalles de la respuesta:'
    cuerpo_texto_2 = f'<table>' \
                    f'<tr><td><strong>Título</strong>:</td> <td>{instance.ticket.titulo}</td></tr>' \
                    f'<tr><td><strong>Tipo</strong>:</td> <td>{instance.ticket.tipo}</td></tr>' \
                    f'<tr><td><strong>Mensaje</strong>:</td> <td>{instance.texto}</td></tr>' \
                    f'<tr><td><strong>Fecha de creación</strong>:</td> <td>{instance.fecha_creacion}</td></tr>' \
                    '</table>'
    Emailer(
        asunto=asunto,
        titulo_texto_1=titulo_texto_1,
        cuerpo_texto_1=cuerpo_texto_1,
        titulo_texto_2=titulo_texto_2,
        cuerpo_texto_2=cuerpo_texto_2,
        destinatarios=[instance.ticket.usuario.email]
    ).enviar()



def notificar_cliente_cambio_estado_ticket(sender, instance, **kwargs):
    asunto = f'Cambio de estado al ticket #{instance.id} - {instance.titulo}'
    titulo_texto_1 = asunto
    cuerpo_texto_1 = f'El estado del ticket ha cambiado a {instance.estado_humanizado}.'
    titulo_texto_2 = 'Detalles del ticket:'
    cuerpo_texto_2 = f'<table>' \
                    f'<tr><td><strong>Título</strong>:</td> <td>{instance.titulo}</td></tr>' \
                    f'<tr><td><strong>Tipo</strong>:</td> <td>{instance.tipo}</td></tr>' \
                    f'<tr><td><strong>Fecha creación</strong>:</td> <td>{instance.fecha_creacion}</td></tr>' \
                    '</table>'
    Emailer(
        asunto=asunto,
        titulo_texto_1=titulo_texto_1,
        cuerpo_texto_1=cuerpo_texto_1,
        titulo_texto_2=titulo_texto_2,
        cuerpo_texto_2=cuerpo_texto_2,
        destinatarios=[instance.usuario.email]
    ).enviar()
