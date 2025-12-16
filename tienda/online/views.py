'pip install djangorestframework'
from django.shortcuts import render, redirect
from online.models import pedidos, categoria, producto
from online.forms import Form_pedido
from django.core.paginator import Paginator

from django.http import JsonResponse
from django.db import models


# Create your views here.

def index(request):
    productos = producto.objects.all()
    paginacion = Paginator(productos, 6)
    pagina = request.GET.get('page', 1)
    obj = paginacion.get_page(pagina)
    categorias = categoria.objects.all()
    data = {'paginacion': obj, 'categorias': categorias}
    return render(request, "index.html", data)

def pedido(request):
    if request.method == "POST":
        form= Form_pedido(request.POST, request.FILES)
        if form.is_valid():
            nuevo_pedido = form.save(commit=False)

            nuevo_pedido.recibido_de= 'Pagina Web'
            nuevo_pedido.estado_de_seguimiento= 'SOL'
            nuevo_pedido.estado_de_pago= 'PEN'

            nuevo_pedido.save()
            return redirect ('seguimiento', token=nuevo_pedido.token)
    else:
        form = Form_pedido()

    pedido = pedidos.objects.all()
    data = {'form': form,
            'pedido': pedido}
    return render(request, "pedidos.html", data)

def reportes_view(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')    

    pedido_query = pedidos.objects.all()
    if fecha_inicio and fecha_fin:
        pedido_query = pedido_query.filter(fecha__range=[fecha_inicio, fecha_fin])

    total_pedidos = pedido_query.count()
    pedidos_por_estado = pedido_query.values('estado_de_seguimiento').annotate(total=models.Count('id')).order_by('estado_de_seguimiento')
    pedidos_por_pago = pedido_query.values('estado_de_pago').annotate(total=models.Count('id')).order_by('estado_de_pago')
    
    # Contar por tipo de pago
    pendientes = pedido_query.filter(estado_de_pago='PEN').count()
    pagados = pedido_query.filter(estado_de_pago='PAG').count()
    parciales = pedido_query.filter(estado_de_pago='PAR').count()

    reporte = {
        'total_pedidos': total_pedidos,
        'pedidos_por_estado': list(pedidos_por_estado),
        'pedidos_por_pago': list(pedidos_por_pago),
        'pendientes': pendientes,
        'pagados': pagados,
        'parciales': parciales,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin
    }

    return render(request, "reportes.html", {'reporte': reporte})

def pedidos_view(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    estados = request.GET.getlist('estados')
    max_resultados = request.GET.get('max_resultados')

    pedidos_filtrados = pedidos.objects.all()

    if fecha_inicio and fecha_fin:
        pedidos_filtrados = pedidos_filtrados.filter(fecha__range=[fecha_inicio, fecha_fin])

    if estados:
        pedidos_filtrados = pedidos_filtrados.filter(estado_de_seguimiento__in=estados)

    if max_resultados:
        pedidos_filtrados = pedidos_filtrados[:int(max_resultados)]

    resultados = [
        {
            'id': pedido.id,
            'token': str(pedido.token),
            'estado_de_seguimiento': pedido.estado_de_seguimiento,
            'fecha': str(pedido.fecha),
        }
        for pedido in pedidos_filtrados
    ]

    return JsonResponse({'pedidos': resultados})

from django.contrib import messages
from .models import pedidos as Pedido

def cancelar_pedido(request, token):
    try:
        pedido = pedidos.objects.get(token=token)
    except pedidos.DoesNotExist:
        messages.error(request, "No se encontró el pedido.")
        return redirect('seguimiento')

    if pedido.estado_de_seguimiento == "FIN":
        messages.warning(request, "El pedido ya estaba cancelado.")
    else:
        pedido.estado_de_seguimiento = "FIN"
        pedido.save()
        messages.success(request, "El pedido fue cancelado con éxito.")

    return redirect('seguimiento', token=token)


def detalle_producto(request, id):
    producto_detalle = producto.objects.get(id=id)
    data = {'producto': producto_detalle}
    return render(request, "detalle_producto.html", data)

def seguimiento(request, token=None):

    token = token or request.GET.get('token')
    error = None
    pedido_detalle = None
    
    if token:
        try:
            pedido_detalle = pedidos.objects.get(token=token)
        except pedidos.DoesNotExist:
            error = "Pedido no encontrado. Verifica tu token."
    else:
        error = "Ingresa un token para buscar tu pedido."
    
    data = {'pedido': pedido_detalle, 'error': error, 'token': token}
    return render(request, "seguimiento.html", data)

###################
#API INSUMO
from .serializers import InsumosSerializer
from .models import insumos
from rest_framework import viewsets

class InsumosViewSet(viewsets.ModelViewSet):
    queryset=insumos.objects.all().order_by('nombre_insumo')
    serializer_class=InsumosSerializer

#API PEDIDOS
from rest_framework import generics
from .serializers import PedidosSerializer

class Crear_Pedido(generics.CreateAPIView):
    queryset=pedidos.objects.all()
    serializer_class= PedidosSerializer

class Modificar_Pedido(generics.UpdateAPIView):
    queryset=pedidos.objects.all()
    serializer_class= PedidosSerializer

