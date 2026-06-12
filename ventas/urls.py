from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetVentas.as_view(), name='ventas'),
    path('<int:id>', views.GetVentaByID.as_view(), name='detalle_venta'),
    path('nueva/', views.CreateVenta.as_view(), name='cargar_venta'),
    path('editar/<int:id>', views.UpdateVenta.as_view(), name='editar_venta'),
    path('anular/<int:id>', views.anularVenta, name='anular_venta'),
]