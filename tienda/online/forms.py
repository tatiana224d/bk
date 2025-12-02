from django import forms
from online.models import pedidos

class Form_pedido(forms.ModelForm):
    fecha = forms.DateField(required=False, widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    class Meta:
        model = pedidos
        fields = '__all__'
        exclude = ('recibido_de', 'estado_de_seguimiento','estado_de_pago', 'token')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@correo.com'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
