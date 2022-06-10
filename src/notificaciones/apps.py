from django.apps import AppConfig
from venta.signals import venta_creada_signal, venta_actualizada_signal, despacho_actualizado_signal
from .venta import (
    notificar_cliente_nueva_compra,
    notificar_admin_nueva_compra,
    notificar_cliente_compra_actualizada,
    notificar_cliente_despacho_actualizado
)

from inventario.signals import producto_poco_stock_signal, producto_agotado_signal
from .inventario import actualizar_inventario, notificar_bodega_poco_stock, notificar_bodega_producto_agotado

from cuenta_usuario.signals import cuenta_empleado_creada
from .cuenta_usuario import notificar_empleado_nueva_cuenta


class NotificacionesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notificaciones'

    def ready(self):

        venta_creada_signal.connect(notificar_cliente_nueva_compra)
        venta_creada_signal.connect(notificar_admin_nueva_compra)
        venta_actualizada_signal.connect(notificar_cliente_compra_actualizada)
        despacho_actualizado_signal.connect(notificar_cliente_despacho_actualizado)

        venta_actualizada_signal.connect(actualizar_inventario)
        venta_creada_signal.connect(actualizar_inventario)
        producto_poco_stock_signal.connect(notificar_bodega_poco_stock)
        producto_agotado_signal.connect(notificar_bodega_producto_agotado)

        cuenta_empleado_creada.connect(notificar_empleado_nueva_cuenta)