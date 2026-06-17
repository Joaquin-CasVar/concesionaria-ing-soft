from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import ClienteForm, PersonaForm, VendedorForm

def registrarse(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        formCli = ClienteForm(request.POST)

        if form.is_valid() and formCli.is_valid():
            usuario = form.save()

            cliente = formCli.save(commit=False)
            cliente.persona = usuario
            cliente.save()

            login(request, usuario)
            return redirect('autos')
    else:
        form = PersonaForm()
        formCli = ClienteForm()

    return render(request, 'registration/register.html', {'form': form, 'formExt': formCli})

def registrarVendedor(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        formVen = VendedorForm(request.POST)

        if form.is_valid() and formVen.is_valid():
            usuario = form.save()

            vendedor = formVen.save(commit=False)
            vendedor.persona = usuario
            vendedor.save()

            return redirect('autos')
    else:
        formVen = VendedorForm()
        form = PersonaForm()
    return render(request, 'registration/register.html', {'form': form, 'formExt': formVen})
