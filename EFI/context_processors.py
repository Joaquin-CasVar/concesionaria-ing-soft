from django.core.cache import cache
from ventas.models import Venta

from datetime import datetime
from collections import Counter

def date_context(request):
    date = datetime.now().date()
    return {'fecha': date}

def marca_popular_context(request):
    ventas = cache.get('ventas_marcas')
    lista_marcas = []

    if ventas is None:
        ventas = Venta.objects.filter(activo=True)
        cache.set('ventas_marcas', ventas, 60*15) # Busca marca mas popular cada 15 mins
        print('Nueva cache')

    for venta in ventas:
        lista_marcas.append(venta.auto.marca.nombre)

    marca_popular = Counter(lista_marcas).most_common()[0][0]

    return {'marca_popular': marca_popular}