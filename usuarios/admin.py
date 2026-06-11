from django.contrib import admin
from .models import Persona, Cliente, Vendedor



@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'telefono')
    search_fields = ('username', 'first_name', 'last_name', 'email')



@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'persona', 'direccion')
    search_fields = ('persona__first_name', 'persona__last_name')



@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'persona', 'salario')
    search_fields = ('persona__first_name', 'persona__last_name')