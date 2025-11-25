from django.contrib import admin
from online.models import pedidos
# Register your models here.

class pedidosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'telefono', 'descripcion', 'producto_ref', 'recibido_de', 'fecha']

admin.site.register(pedidos, pedidosAdmin)
