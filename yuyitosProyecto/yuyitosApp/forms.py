from django import forms
from django.db.models import fields
from .models import Fiado, Cliente, Producto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre','apellido','estado') 


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigoProducto','nombre','familia_producto','descripcion','estado','precio_costo','precio_venta')
        
class FiadoForm(forms.ModelForm):
    class Meta:
        model = Fiado
        fields = ('monto', 'abono','estado', 'fecha_inicio', 'fecha_final', 'cliente' )