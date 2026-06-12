from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Venta
from .forms import VentaForm

class GetVentas(ListView):
    model = Venta
    template_name = 'ventas/index.html'
    context_object_name = 'ventas'

class GetVentaByID(DetailView):
    model = Venta
    template_name = 'ventas/detalle_venta.html'
    context_object_name = 'venta'

class CreateVenta(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'ventas/cargar_venta.html'
    success_url = reverse_lazy('ventas')

class UpdateVenta(UpdateView):
    model = Venta
    form_class = VentaForm
    template_name = 'ventas/editar_venta.html'
    success_url = reverse_lazy('ventas')


def anularVenta(request, id):
    venta = get_object_or_404(Venta, id=id)

    if request.method == 'POST':
        venta.activo = False
        venta.save()

        return redirect('ventas')
    
    return render(request, 'ventas/eliminar_venta.html', {'venta': venta})
