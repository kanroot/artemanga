from venta.enums.opciones import EstadoVenta
from .emailer import Emailer


def actualizar_inventario(sender, instance, **kwargs):
    match instance.estado:
        case EstadoVenta.PENDIENTE.value:
            # se asume nueva venta, actualizamos inventario para reducir cantidad:
            for venta_producto in instance.detalles:
                venta_producto.producto.stock -= venta_producto.cantidad
                venta_producto.producto.save()
        case EstadoVenta.CANCELADA.value:
            # se canceló la venta, recuperamos el stock reservado:
            for venta_producto in instance.detalles:
                venta_producto.producto.stock += venta_producto.cantidad
                venta_producto.producto.save()
        case _:
            # los otros estados no nos importan
            pass


def notificar_bodega_poco_stock(sender, instance, **kwargs):
    from cuenta_usuario.models import Usuario
    from cuenta_usuario.enums.opciones import TipoUsuario
    bodegas = Usuario.objects.filter(tipo_usuario=TipoUsuario.BODEGA.value)
    asunto = 'Producto con poco stock!'
    titulo_texto_1 = asunto
    cuerpo_texto_1 = f'EL Producto {instance.titulo_es} tiene poco stock!'
    titulo_texto_2 = 'Detalles del Producto:'
    cuerpo_texto_2 = f'<table>' \
                    f'<tr><td><strong>Título</strong>:</td> <td>{instance.titulo_es}</td></tr>' \
                    f'<tr><td><strong>Stock actual</strong>:</td> <td>{instance.stock}</td></tr>' \
                    '</table>'

    Emailer(
        asunto=asunto,
        titulo_texto_1=titulo_texto_1,
        cuerpo_texto_1=cuerpo_texto_1,
        titulo_texto_2=titulo_texto_2,
        cuerpo_texto_2=cuerpo_texto_2,
        destinatarios=[bodega.email for bodega in bodegas]
    ).enviar()




def notificar_bodega_producto_agotado(sender, instance, **kwargs):
    from cuenta_usuario.models import Usuario
    from cuenta_usuario.enums.opciones import TipoUsuario
    bodegas = Usuario.objects.filter(tipo_usuario=TipoUsuario.BODEGA.value)
    asunto = 'Producto con poco stock!'
    titulo_texto_1 = asunto
    cuerpo_texto_1 = f'EL Producto {instance.titulo_es} se ha agotado!'
    titulo_texto_2 = 'Detalles del Producto:'
    cuerpo_texto_2 = f'<table>' \
                    f'<tr><td><strong>Título</strong>:</td> <td>{instance.titulo_es}</td></tr>' \
                    f'<tr><td><strong>Stock actual</strong>:</td> <td>{instance.stock}</td></tr>' \
                    '</table>'

    Emailer(
        asunto=asunto,
        titulo_texto_1=titulo_texto_1,
        cuerpo_texto_1=cuerpo_texto_1,
        titulo_texto_2=titulo_texto_2,
        cuerpo_texto_2=cuerpo_texto_2,
        destinatarios=[bodega.email for bodega in bodegas]
    ).enviar()
