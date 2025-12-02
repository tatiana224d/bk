from django.shortcuts import render, redirect
from online.models import pedidos
from online.models import categoria
from online.forms import Form_pedido
# Create your views here.

def index(request):
    categorias= categoria.objects.all()
    data = {'categorias': categorias}
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
            return redirect ('pedido')
    else:
        form = Form_pedido()

    pedido = pedidos.objects.all()
    data = {'form': form,
            'pedido': pedido}
    return render(request, "pedidos.html", data)
