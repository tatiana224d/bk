from django.shortcuts import render
from online.models import pedidos, categoria, producto
from online.forms import Form_pedido
# Create your views here.

def index(request):
    productos = producto.objects.all()
    categorias = categoria.objects.all()
    data = {'productos': productos, 'categorias': categorias}
    return render(request, "index.html", data)

def pedido(request):
    if request.method == "post":
        form= Form_pedido(request.post, request.FILES)
        if form.is_valid():
            form.save()
            return pedidos(request)
    else:
        form = Form_pedido()

    pedido = pedidos.objects.all()
    data = {'form': form,
            'pedido': pedido}
    return render(request, "pedidos.html", data)

def detalle_producto(request, id):
    producto_detalle = producto.objects.get(id=id)
    data = {'producto': producto_detalle}
    return render(request, "detalle_producto.html", data)