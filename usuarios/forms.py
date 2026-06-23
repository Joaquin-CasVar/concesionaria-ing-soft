from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente, Persona, Vendedor

class PersonaForm(UserCreationForm):
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

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['direccion', ]
        widgets = {
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su dirección'
            }),
        }

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['salario', ]
        widgets = {
            'salario': forms.NumberInput(attrs={'class': 'form-control'}),
        }
