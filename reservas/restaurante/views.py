from rest_framework import viewsets
from django.shortcuts import render

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

from .serializers import (
    RestauranteSerializer,
    SucursalSerializer,
    ClienteSerializer,
    MesaSerializer,
    EstadoReservaSerializer,
    ReservaSerializer,
    MetodoPagoSerializer,
    PagoSerializer
)


class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer


class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer


class EstadoReservaViewSet(viewsets.ModelViewSet):
    queryset = EstadoReserva.objects.all()
    serializer_class = EstadoReservaSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


class MetodoPagoViewSet(viewsets.ModelViewSet):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    
def inicio(request):
    return render(request, 'bienvenida.html')