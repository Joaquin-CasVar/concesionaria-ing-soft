from django.contrib import admin
from .models import Auto, Marca, TipoCombustible, TipoTransmision, TipoDireccion, Color

admin.site.register(Marca)
admin.site.register(TipoCombustible)
admin.site.register(TipoTransmision)
admin.site.register(TipoDireccion)
admin.site.register(Color)

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'marca', 'anio', 'nuevo', 'activo')
    list_filter = ('marca', 'nuevo', 'activo')
    search_fields = ('nombre', 'patente')