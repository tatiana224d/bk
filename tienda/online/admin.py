from django.contrib import admin
from online.models import pedidos, categoria, producto, insumos
# Register your models here.

class pedidosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'telefono', 'descripcion', 'producto_ref', 'recibido_de', 'fecha', 'estado_pago', 'estado_seguimiento']
    list_filter= ['estado_pago', 'estado_seguimiento']
    search_fields= ['nombre','email']
    def producto_ref (self,obj):
        if obj. roducto.ref:
            return format_html('<img src="{}" width="100" height="100" />', obj.producto_ref.url)
        return "Sin imagen"
    
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


