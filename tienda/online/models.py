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



