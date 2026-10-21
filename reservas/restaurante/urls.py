from rest_framework.routers import DefaultRouter

from .views import (
    RestauranteViewSet,
    SucursalViewSet,
    ClienteViewSet,
    MesaViewSet,
    EstadoReservaViewSet,
    ReservaViewSet,
    MetodoPagoViewSet,
    PagoViewSet
)

router = DefaultRouter()

router.register(r'restaurantes', RestauranteViewSet)
router.register(r'sucursales', SucursalViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'mesas', MesaViewSet)
router.register(r'estados-reserva', EstadoReservaViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'metodos-pago', MetodoPagoViewSet)
router.register(r'pagos', PagoViewSet)

urlpatterns = router.urls