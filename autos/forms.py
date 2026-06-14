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
        widgets = {
            'marca': forms.Select(attrs={'class': 'form-select'}),
            'combustible': forms.Select(attrs={'class': 'form-select'}),
            'transmision': forms.Select(attrs={'class': 'form-select'}),
            'direccion': forms.Select(attrs={'class': 'form-select'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'turbo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control'}),
            'nuevo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'kilometros': forms.NumberInput(attrs={'class': 'form-control'}),
            'patente': forms.TextInput(attrs={'class': 'form-control'}),
            'puertas': forms.NumberInput(attrs={'class': 'form-control'}),
            'marchas': forms.NumberInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }