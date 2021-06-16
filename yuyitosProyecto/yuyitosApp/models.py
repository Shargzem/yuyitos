from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BooleanField, CharField, DateTimeField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.core.validators import MinValueValidator

# Create your models here.
class Administrador(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre



class Pedido(models.Model):
    idPedido = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    total = models.IntegerField()
    precio = models.IntegerField()
    modificacion = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.idPedido



class Proveedor(models.Model):
    rutEmpresa = models.CharField(max_length=10)
    razon_social = models.CharField(max_length=100)
    giro = models.CharField(max_length=100)
    telefono = models.IntegerField()
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rutEmpresa



class Tipo_producto(models.Model):
    idTipoProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.idTipoProducto



class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    codigoProducto = models.BigIntegerField()
    nombre = models.CharField(max_length=100)
    familia_producto = CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    fecha_vencimiento = models.DateTimeField()
    estado = models.BooleanField()
    precio_costo = models.IntegerField()
    precio_venta = models.IntegerField()
    modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Pedido_producto(models.Model):
    idPedidoProducto = models.AutoField(primary_key=True)

    def __str__(self):
        return self.idPedidoProducto



class Venta_detalle(models.Model):
    idVentaDetalle = models.AutoField(primary_key=True)
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    monto = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    monto_total = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now=True)
    modificacion = models.DateTimeField(auto_now=True)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, default=1)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, default=9)

    

    def __int__(self):
        return self.idVentaDetalle


class Metodo_pago(models.Model):
    idMetodoPago = models.AutoField(primary_key=True)
    tipoPago = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.tipoPago


class Boleta(models.Model):
    idBoleta = models.AutoField(primary_key=True)
    folio = models.IntegerField(default=2)
    fecha = models.DateTimeField()
    modificacion = models.DateTimeField(auto_now=True)
    tipo_pago = models.CharField(max_length=100)
    estado = models.BooleanField()

    def __str__(self):
        return self.idBoleta


class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    estado = models.BooleanField()
    modificacion = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.nombre


class Fiado(models.Model):
    idFiado = models.AutoField(primary_key=True)
    monto = models.IntegerField()
    abono = models.IntegerField()
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    modificacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField()
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, default=9)

    def __int__(self):
        return self.idFiado