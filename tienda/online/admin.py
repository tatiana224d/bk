from django.contrib import admin
from online.models import pedidos, categoria, producto, insumos
from django.utils.html import format_html
# Register your models here.

class pedidosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'telefono', 'descripcion', 'producto_ref', 'recibido_de', 'fecha']

class categoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre_categoria', 'slug']
    prepopulated_fields = {'slug': ('nombre_categoria',)}


class productoAdmin(admin.ModelAdmin):
    list_display = ['nombre_producto', 'precio_producto', 'categoria']

class insumosAdmin(admin.ModelAdmin):
    list_display = ['nombre_insumo', 'tipo_insumo', 'cantidad_disponible', 'unidad_medida', 'marca_insumo', 'color_insumo']

admin.site.register(pedidos, pedidosAdmin)
admin.site.register(categoria, categoriaAdmin)
admin.site.register(producto, productoAdmin)
admin.site.register(insumos, insumosAdmin)

