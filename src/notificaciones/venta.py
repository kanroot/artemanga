from .emailer import Emailer


def notificar_cliente_nueva_compra(sender, instance, **kwargs):
    asunto = '¡Muchas gracias por tu compra!'
    titulo_texto_1 = asunto
    cuerpo_texto_1 = f'Hola {instance.usuario.username}, muchas gracias por tu compra en ArteManga.cl\n' \
                    f'En breve uno de nuestros administradores validará la transferencia y comenzará el proceso de envío.\n' \
                    f'Te mantendremos informado sobre cualquier novedad mediante correo, así que por favor ¡Quédate atento!.\n' \
                    f'También puedes ver el estado de tu compra iniciando sesión y yendo a "Mis Pedidos".\n'
    titulo_texto_2 = 'Detalles de tu compra'
    cuerpo_texto_2 = f'<table>' \
                    f'<tr><td><strong>Compra nº</strong>:</td> <td>{instance.pk}</td></tr>' \
                    f'<tr><td><strong>Productos</strong>:</td> <td>{", ".join(str(compra.producto) for compra in instance.detalles)}</td></tr>' \
                    f'<tr><td><strong>Total</strong>:</td> <td>${instance.total_humanizado}</td></tr>' \
                    f'</table>'
    Emailer(
        asunto=asunto,
        titulo_texto_1=titulo_texto_1,
        cuerpo_texto_1=cuerpo_texto_1,
        titulo_texto_2=titulo_texto_2,
        cuerpo_texto_2=cuerpo_texto_2,
        destinatarios=[instance.usuario.email]
    ).enviar()


def notificar_admin_nueva_compra(sender, instance, **kwargs):
    from cuenta_usuario.models import Usuario
    from cuenta_usuario.enums.opciones import TipoUsuario
    admins = Usuario.objects.filter(tipo_usuario=TipoUsuario.VENTAS.value)
    asunto = 'Nueva compra'
    titulo_texto_1 = asunto
    cuerpo_texto_1 = f'Se ha realizado una nueva compra en ArteManga.cl\n' \
                    f'Para ver los detalles de la compra y validarla, ingresa a tu cuenta de usuario.\n'
    titulo_texto_2 = 'Detalles de la compra'
    cuerpo_texto_2 = f'<table>' \
                    f'<tr><td><strong>Compra nº</strong>:</td> <td>{instance.pk}</td></tr>' \
                    f'<tr><td><strong>Productos</strong>:</td> <td>{", ".join(str(compra.producto) for compra in instance.detalles)}</td></tr>' \
                    f'<tr><td><strong>Total</strong>:</td> <td>${instance.total_humanizado}</td></tr>' \
                    f'</table>'
    Emailer(
        asunto=asunto,
        titulo_texto_1=titulo_texto_1,
        cuerpo_texto_1=cuerpo_texto_1,
        titulo_texto_2=titulo_texto_2,
        cuerpo_texto_2=cuerpo_texto_2,
        destinatarios=[admin.email for admin in admins]
    ).enviar()


def notificar_cliente_compra_actualizada(sender, instance, **kwargs):
    from venta.enums.opciones import EstadoVenta

    match instance.estado:
        case EstadoVenta.PENDIENTE.value:
            asunto = 'Tu compra ha vuelto a estado pendiente'
            titulo_texto_1 = asunto
            cuerpo_texto_1 = f'Hola {instance.usuario.username}, tu compra ha vuelto a estar pendiente.\n' \
                            f'Por favor espera un poco más a que terminemos de validarla.\n' \
                            f'Si quieres más detalles sobre el motivo de este cambio, inicia un ticket en nuestro ' \
                            f'<a href="#">portal de soporte</a>.\n'
        case EstadoVenta.APROBADA.value:
            asunto = '¡Tu compra ha sido aprobada!'
            titulo_texto_1 = asunto
            cuerpo_texto_1 = f'Hola {instance.usuario.username}, tu compra ha sido validada y aprobada por uno de nuestros administradores.\n' \
                            f'Ahora mismo, hemos comenzado el proceso de empaquetado y envío, así que quédate atento porque te avisaremos una vez\n' \
                            f'que tu pedido esté en manos de nuestro courier.\n'
        case EstadoVenta.CANCELADA.value:
            asunto = '¡Oops, parece que hubo un problema con tu compra!'
            titulo_texto_1 = asunto
            cuerpo_texto_1 = f'Hola {instance.usuario.username}, lamentamos informarte que tu compra ha sido cancelada.\n' \
                            f'Si crees que es un error, por favor inicia un ticket en nuestro <a href="#">portal de soporte</a> para que podamos ayudarte.\n'
        case _:
            raise ValueError('Estado de venta no válido: ', instance.estado)

    titulo_texto_2 = 'Detalles de tu compra'
    cuerpo_texto_2 = f'<table>' \
                    f'<tr><td><strong>Compra nº</strong>:</td> <td>{instance.pk}</td></tr>' \
                    f'<tr><td><strong>Productos</strong>:</td> <td>{", ".join(str(compra.producto) for compra in instance.detalles)}</td></tr>' \
                    f'<tr><td><strong>Total</strong>:</td> <td>${instance.total_humanizado}</td></tr>' \
                    f'</table>'

    Emailer(
        asunto=asunto,
        titulo_texto_1=titulo_texto_1,
        cuerpo_texto_1=cuerpo_texto_1,
        titulo_texto_2=titulo_texto_2,
        cuerpo_texto_2=cuerpo_texto_2,
        destinatarios=[instance.usuario.email]
    ).enviar()


def notificar_cliente_despacho_actualizado(sender, instance, **kwargs):
    from venta.enums.opciones import EstadoDes

    match instance.estado:
        case EstadoDes.PENDIENTE.value:
            asunto = 'Tu despacho ha vuelto a estar pendiente'
            titulo_texto_1 = asunto
            cuerpo_texto_1 = f'Hola {instance.usuario.username}, tu despacho ha vuelto a estar pendiente.\n' \
                            f'Por favor espera un poco más a que terminemos de validarlo.\n' \
                            f'Si quieres más detalles sobre el motivo de este cambio, inicia un ticket en nuestro ' \
                            f'<a href="#">portal de soporte</a>.\n'
        case EstadoDes.EN_PROCESO.value:
            asunto = '¡Tu pedido va en camino!'
            titulo_texto_1 = asunto
            cuerpo_texto_1 = f'Hola {instance.usuario.username}, ya pusimos todo en la caja y va en camino a tu casa.\n' \
                            f'Puedes seguir el envío mediante el siguiente código de seguimiento: <strong>{instance.codigo_seguimiento}</strong> en ' \
                            f'<a href="#">la página de Starken.</a>\n'

        case EstadoDes.FALLIDO.value:
            asunto = '¡Oops, parece que hubo un problema con tu despacho!'
            titulo_texto_1 = asunto
            cuerpo_texto_1 = f'Hola {instance.usuario.username}, lamentamos informarte que hubo un problema con tu despacho.\n' \
                            f'Utiliza el código de seguimiento: <strong>{instance.codigo_seguimiento}</strong> en <a href="#">la página de Starken.</a>' \
                            f'para conocer más detalles.\n' \
                            f'Si necesitas más ayuda, siempre puedes iniciar un ticket en nuestro <a href="#">portal de soporte</a> para que podamos guiarte.\n'
        case EstadoDes.FINALIZADO.value:
            asunto = '¡Entregamos tu paquete!'
            titulo_texto_1 = asunto
            cuerpo_texto_1 = f'Hola {instance.usuario.username}, según nos informa nuestro provedor, tu pedido está en tus manos.\n' \
                            f'Utiliza el código de seguimiento: <strong>{instance.codigo_seguimiento}</strong> en <a href="#">la página de Starken.</a>' \
                            f'para conocer más detalles.\n' \
                            f'Si necesitas más ayuda, siempre puedes iniciar un ticket en nuestro <a href="#">portal de soporte</a> para que podamos guiarte.\n'
        case _:
            raise ValueError('Estado de despacho no válido: ', instance.estado)

    titulo_texto_2 = 'Detalles de tu despacho'
    cuerpo_texto_2 = f'<table>' \
                    f'<tr><td><strong>Despacho nº</strong>:</td> <td>{instance.pk}</td></tr>' \
                    f'<tr><td><strong>Dirección</strong>:</td> <td>{instance.direccion}</td></tr>' \
                    f'<tr><td><strong>Código de seguimiento</strong>:</td> <td>{instance.codigo_seguimiento}</td></tr>' \
                    f'</table>'

    Emailer(
        asunto=asunto,
        titulo_texto_1=titulo_texto_1,
        cuerpo_texto_1=cuerpo_texto_1,
        titulo_texto_2=titulo_texto_2,
        cuerpo_texto_2=cuerpo_texto_2,
        destinatarios=[instance.usuario.email]
    ).enviar()
