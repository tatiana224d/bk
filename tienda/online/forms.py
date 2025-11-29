from django import forms
from online.models import pedidos

class Form_pedido(forms.ModelForm):
    class Meta: #nos dice cual va a ser el modelo que queremos ocupar.
        model = pedidos
        fields ='__all__'

'''class Form_pedido(forms.ModelForm):
    class Meta:
        model = pedidos
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@correo.com'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
'''