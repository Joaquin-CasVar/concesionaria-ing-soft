from django import forms

from .models import Venta, MetodoPago

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = [
            'auto',
            'vendedor',
            'cliente',
            'metodoPago',
            'fecha',
            'precio',
        ]
