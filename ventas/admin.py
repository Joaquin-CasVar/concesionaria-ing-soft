from django.contrib import admin

from .models import Venta, MetodoPago

admin.site.register(MetodoPago)

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'auto', 'vendedor', 'fecha', 'precio', 'activo')
    list_filter = ('vendedor', 'fecha')
    search_fields = ('auto__nombre',)