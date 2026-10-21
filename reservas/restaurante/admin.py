from django.contrib import admin

from .models import (
    Restaurante,
    Sucursal,
    Cliente,
    Mesa,
    EstadoReserva,
    Reserva,
    MetodoPago,
    Pago
)

admin.site.register(Restaurante)
admin.site.register(Sucursal)
admin.site.register(Cliente)
admin.site.register(Mesa)
admin.site.register(EstadoReserva)
admin.site.register(Reserva)
admin.site.register(MetodoPago)
admin.site.register(Pago)