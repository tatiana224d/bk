from django.shortcuts import render
from online.models import pedidos
# Create your views here.

def index(request):
    pedido = pedidos.objects.all()
    data = {'pedido': pedido}
    return render(request, "index.html", data)