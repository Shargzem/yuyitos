from django.contrib import admin

from .models import Administrador, Pedido, Proveedor, Producto, Venta_detalle, Tipo_producto, Pedido_producto, Metodo_pago, Boleta, Cliente, Fiado
# Register your models here.


admin.site.register(Administrador)
admin.site.register(Pedido)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Venta_detalle)
admin.site.register(Tipo_producto)
admin.site.register(Pedido_producto)
admin.site.register(Metodo_pago)
admin.site.register(Boleta)
admin.site.register(Cliente) 
admin.site.register(Fiado)

