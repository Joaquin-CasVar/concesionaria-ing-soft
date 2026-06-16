from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import PersonaForm
from .models import Cliente

def registrarse(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            Cliente.objects.create(
                persona=usuario,
                direccion=form.cleaned_data['direccion']
            )
            login(request, usuario)
            return redirect('autos')
    else:
        form = PersonaForm()
    return render(request, 'registration/register.html', {'form': form})