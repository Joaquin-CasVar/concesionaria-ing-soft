from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Venta
from .forms import VentaForm
from autos.views import eliminar_auto
from autos.models import Auto

@login_required
@permission_required('ventas.view_venta')
def getVentas(request):
    ventas = Venta.objects.filter(activo=True)
    return render(request, 'ventas/index.html', {'ventas': ventas})

class GetVentaByID(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Venta
    template_name = 'ventas/detalle_venta.html'
    context_object_name = 'venta'
    permission_required = 'ventas.view_venta'

@login_required
@permission_required('ventas.add_venta')
def createVenta(request):
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            eliminar_auto(request, id=form.data['auto'])
            return redirect('ventas')
    else:
        form = VentaForm()
    
    return render(request, 'ventas/cargar_venta.html', {'form': form})

class UpdateVenta(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Venta
    form_class = VentaForm
    template_name = 'ventas/editar_venta.html'
    success_url = reverse_lazy('ventas')
    permission_required = 'ventas.change_venta'


@login_required
@permission_required('ventas.delete_venta')
def anularVenta(request, id):
    venta = get_object_or_404(Venta, id=id)

    if request.method == 'POST':
        venta.activo = False
        venta.save()

        auto = get_object_or_404(Auto, id=venta.auto.id)
        auto.activo = True
        auto.save()

        return redirect('ventas')
    
    return render(request, 'ventas/eliminar_venta.html', {'venta': venta})
