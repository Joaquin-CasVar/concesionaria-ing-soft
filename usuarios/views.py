from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import PersonaForm

def registrarse(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('autos')
    else:
        form = PersonaForm()
    return render(request, 'usuarios/registrarse.html', {'form': form})