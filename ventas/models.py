from django.db import models

from usuarios.models import Cliente, Vendedor
from autos.models import Auto

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=50,)
    activo = models.BooleanField(default=True,)
    
    def __str__(self):
        return f'Metodo de pago: {self.nombre}'

    class Meta:
        verbose_name = 'metodo de pago'
        verbose_name_plural = 'metodos de pago'

class Venta(models.Model):
    auto = models.ForeignKey(
        Auto,
        on_delete=models.CASCADE,
        verbose_name='el auto a vender',
    )
    vendedor = models.ForeignKey(
        Vendedor,
        on_delete=models.CASCADE,
        verbose_name='responsable de la venta',
    )
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
    )
    metodoPago = models.ForeignKey(
        MetodoPago,
        on_delete=models.CASCADE,
        verbose_name='metodo de pago',
    )
    precio = models.FloatField('precio del auto',)
    fecha = models.DateField('fecha de la venta',)
    activo = models.BooleanField(default=True,)

    def __str__(self):
        return f'Venta N°{self.pk}'
