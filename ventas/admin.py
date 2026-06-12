from django.contrib import admin

from .models import Venta, MetodoPago

admin.site.register(Venta)
admin.site.register(MetodoPago)

# @admin.register(Venta)
# class VentaAdmin(admin.ModelAdmin):
#     ...