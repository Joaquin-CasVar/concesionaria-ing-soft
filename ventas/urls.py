from django.urls import path
from . import views

urlpatterns = [
    path('', views.getVentas, name='ventas'),
    path('<int:pk>', views.GetVentaByID.as_view(), name='detalle_venta'),
    path('nueva/', views.createVenta, name='cargar_venta'),
    path('editar/<int:pk>', views.UpdateVenta.as_view(), name='editar_venta'),
    path('anular/<int:id>', views.anularVenta, name='anular_venta'),
]