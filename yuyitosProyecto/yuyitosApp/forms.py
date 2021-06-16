from django import forms
from django.db.models import fields
from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelect
from .models import Fiado, Cliente, Producto, Venta_detalle, Metodo_pago

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre','apellido','estado') 



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigoProducto','nombre','familia_producto','descripcion','estado', 'fecha_vencimiento','precio_costo','precio_venta')
        widgets = {
            "fecha_vencimiento": forms.SelectDateWidget(),
            
        }
        


class FiadoForm(forms.ModelForm):
    class Meta:
        model = Fiado
        fields = ('__all__' )

        widgets = {
            "fecha_inicio": forms.SelectDateWidget(),
            "fecha_final": forms.SelectDateWidget()
        }


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta_detalle
        fields = ('__all__')

        