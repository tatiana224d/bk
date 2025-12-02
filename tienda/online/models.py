from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class pedidos(models.Model):

    nombre = models.CharField(max_length=120)
    email =models.CharField(max_length=120)
    telefono =models.PositiveIntegerField(null= True, blank= True)#numero de telefono
    descripcion=models.TextField(max_length=120, blank=True)
    producto_ref =models.ImageField(upload_to="media/", blank=True) #imagen de producto de referencia
    recibido_de = models.CharField(max_length=120) #wsp, o presencial
    fecha=models.DateField(null=True) #fecha para la que se necesita el producto

#ESTADOS
    estado_pedidos = [
        ('SOL', 'SOLICITADO'),
        ('APR', 'APROBADO'),
        ('EN', 'EN PROCESO'),
        ('REA', 'REALIZADO'),
        ('FIN', 'FINALIZADO'),
        ('ENT', 'ENTREGADO'),
    ]
    
    estado_pago = [
        ('PEN' , 'PENDIENTE'),
        ('PAR', 'PARCIAL'),
        ('PAG' , 'PAGADO'),
    ]
    
    estado_seguimiento = models.CharField(max_length=3, choices= estado_pedidos, default="SOL" )
    estado_pago = models.CharField(max_length=3, choices= estado_pago, default="PEN")
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.nombre


    def __str__(self):
        return f"{self.nombre} - {self.token}"

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