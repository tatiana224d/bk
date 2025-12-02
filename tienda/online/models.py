from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class pedidos(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('procesando', 'Procesando'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]
    
    nombre = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    telefono = models.PositiveIntegerField(blank=True)
    token = models.CharField(max_length=120, default=uuid.uuid4, unique=True)
    descripcion = models.TextField(max_length=120, blank=True)
    producto_ref = models.ImageField(blank=False, upload_to='pedido_images/')
    recibido_de = models.CharField(max_length=120)
    fecha = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

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