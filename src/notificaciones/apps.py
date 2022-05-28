from django.apps import AppConfig
from venta.signals import venta_creada_signal, venta_actualizada_signal, despacho_actualizado_signal
from .venta import (
    notificar_cliente_nueva_compra,
    notificar_admin_nueva_compra,
    notificar_cliente_compra_actualizada,
    notificar_cliente_despacho_actualizado
)


class NotificacionesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notificaciones'

    def ready(self):
        venta_creada_signal.connect(notificar_cliente_nueva_compra)
        venta_creada_signal.connect(notificar_admin_nueva_compra)
        venta_actualizada_signal.connect(notificar_cliente_compra_actualizada)
        despacho_actualizado_signal.connect(notificar_cliente_despacho_actualizado)

