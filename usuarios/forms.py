from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Persona

class PersonaForm(UserCreationForm):
    class Meta:
        model = Persona
        fields = ['username', 'first_name', 'last_name', 'email', 'telefono']