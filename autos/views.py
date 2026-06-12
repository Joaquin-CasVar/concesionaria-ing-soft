from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Auto
from .forms import AutoForm


def listar_autos(request):
    autos = Auto.objects.filter(activo=True)
    return render(request, 'autos/index.html', {'autos': autos})


@login_required
@permission_required('autos.add_auto')
def crear_auto(request):
    if request.method == 'POST':
        form = AutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('autos')
    else:
        form = AutoForm()
    return render(request, 'autos/crear_auto.html', {'form': form})


@login_required
@permission_required('autos.change_auto')
def editar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'POST':
        form = AutoForm(request.POST, request.FILES, instance=auto)
        if form.is_valid():
            form.save()
            return redirect('autos')
    else:
        form = AutoForm(instance=auto)
    return render(request, 'autos/editar_auto.html', {'form': form})


@login_required
@permission_required('autos.delete_auto')
def eliminar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'POST':
        auto.activo = False
        auto.save()
        return redirect('autos')
    return render(request, 'autos/eliminar_auto.html', {'auto': auto})