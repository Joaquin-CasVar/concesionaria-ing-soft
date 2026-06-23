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
        widgets = {
            'auto': forms.Select(attrs={'class': 'form-select'}),
            'vendedor': forms.Select(attrs={'class': 'form-select'}),
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'metodoPago': forms.Select(attrs={'class': 'form-select'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }
