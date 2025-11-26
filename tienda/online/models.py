from django.db import models

# Create your models here.

class pedidos(models.Model):
    nombre = models.CharField(max_length=120)
    email =models.CharField(max_length=120)
    telefono =models.PositiveIntegerField(blank=True) #numero de telefono

    descripcion=models.TextField(max_length=120, blank=True)
    producto_ref =models.ImageField(blank= False) #imagen de producto de referencia
    recibido_de = models.CharField(max_length=120) #wsp, o presencial

    fecha=models.DateField() #fecha para la que se necesita el producto
    def __str__(self):
        return self.nombre
    
class catalogo(models.Model):
    nombre_producto = models.CharField(max_length=120)
    descripcion_producto = models.TextField(max_length=250)
    imagen_producto = models.ImageField(upload_to='product_images/')
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_producto