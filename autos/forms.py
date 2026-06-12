from django import forms
from .models import Auto

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = (
            'marca',
            'combustible',
            'transmision',
            'direccion',
            'color',
            'nombre',
            'turbo',
            'anio',
            'nuevo',
            'kilometros',
            'patente',
            'puertas',
            'marchas',
            'foto',
        )