from rest_framework import serializers
from online.models import insumos
from online.models import pedidos

class InsumosSerializer(serializers.ModelSerializer):
    class Meta:
        model= insumos
        fields= '__all__'

class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = pedidos
        fields= ('nombre', 'email', 'telefono', 'producto_ref', 'fecha') #puede modificar, para que pueda crear tendria que ir al formulario ¿no?
        read_only_fields= ('id'),


