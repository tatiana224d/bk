from django.db import models
import uuid

# Create your models here.  28:42

class pedidos(models.Model):
    nombre = models.CharField(max_length=120)
    email =models.CharField(max_length=120)
    telefono =models.PositiveIntegerField(blank=True) #numero de telefono
    token=models.CharField(max_length=120, default=uuid.uuid4) #token de pago
    descripcion=models.TextField(max_length=120, blank=True)
    producto_ref =models.ImageField(blank= False) #imagen de producto de referencia
    recibido_de = models.CharField(max_length=120) #wsp, o presencial
    fecha=models.DateField() #fecha para la que se necesita el producto

    def seguimiento(request,render):
        token=request.GET.get('token')
        try:
            pedido=pedidos.objects.get(token=token)
            return render (request, 'seguimiento.html', {'pedido': pedido})
        except pedidos.DoesNotExist:
            return render (request, 'seguimiento.html', {'error': 'Pedido no encontrado'})

    def __str__(self):
        return self.nombre
    
class categoria(models.Model):
    nombre_categoria = models.CharField(max_length=120)
    slug=models.SlugField()

    def __str__(self):
        return self.nombre_categoria   
    
class producto(models.Model):
    nombre_producto = models.CharField(max_length=120)
    descripcion_producto = models.TextField(max_length=250)
    imagen_producto = models.ImageField(upload_to='product_images/')
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2) 
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto

class insumos(models.Model):
    nombre_insumo = models.CharField(max_length=120)
    tipo_insumo = models.CharField(max_length=120)
    cantidad_disponible = models.PositiveIntegerField()
    unidad_medida = models.CharField(max_length=50, blank=True)
    marca_insumo = models.CharField(max_length=120)
    color_insumo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_insumo