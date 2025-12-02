from django.shortcuts import render, redirect
from online.models import pedidos, categoria, producto
from online.forms import Form_pedido
from django.core.paginator import Paginator
import uuid
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
            nuevo_pedido.estado_seguimiento= 'SOL'
            nuevo_pedido.estado_pago= 'PEN'

            nuevo_pedido.save()
            return redirect ('seguimiento', token=nuevo_pedido.token)
    else:
        form = Form_pedido()

    pedido = pedidos.objects.all()
    data = {'form': form,
            'pedido': pedido}
    return render(request, "pedidos.html", data)


from django.contrib import messages
from .models import pedidos

def cancelar_pedido(request, token):
    try:
        pedido = Pedido.objects.get(token=token)
    except Pedido.DoesNotExist:
        messages.error(request, "No se encontró el pedido.")
        return redirect('seguimiento')

    if pedido.estado == "Cancelado":
        messages.warning(request, "El pedido ya estaba cancelado.")
    else:
        pedido.estado = "Cancelado"
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

