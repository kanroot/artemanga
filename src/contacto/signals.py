from django.dispatch import Signal

nuevo_ticket_signal = Signal()
estado_ticket_cambiado_signal = Signal()
nuevo_mensaje_admin_signal = Signal()
nuevo_mensaje_cliente_signal = Signal()