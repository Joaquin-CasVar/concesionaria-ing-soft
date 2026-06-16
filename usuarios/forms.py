from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Persona

class PersonaForm(UserCreationForm):
    direccion = forms.CharField(
        max_length=255,
        required=True,
        label='Dirección',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su dirección'})
    )

    class Meta:
        model = Persona
        fields = ['username', 'first_name', 'last_name', 'email', 'telefono']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'