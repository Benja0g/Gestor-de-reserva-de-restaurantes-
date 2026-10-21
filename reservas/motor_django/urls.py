from django.contrib import admin
from django.urls import path, include
from restaurante.views import inicio

urlpatterns = [
    path('', inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('api/', include('restaurante.urls')),
]