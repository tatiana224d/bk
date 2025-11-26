from django.contrib import admin
from online.models import pedidos, catalogo
# Register your models here.

class pedidosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'telefono', 'descripcion', 'producto_ref', 'recibido_de', 'fecha']

admin.site.register(pedidos, pedidosAdmin)

@admin.register(catalogo)
class catalogoAdmin(admin.ModelAdmin):
    list_display = ['nombre_producto', 'precio_producto']

