from django.http import request
from django.shortcuts import redirect, render
from .models import Fiado, Cliente, Producto
from .forms import FiadoForm, ClienteForm, ProductoForm
from django.contrib import messages
# Create your views here.

#se envia data como un diccionario(contexto)

def inicio(request):
    return render(request, 'inicio.html')


#Begin Cliente

def listado_cliente(request):
    clientes = Cliente.objects.all()   #select * from Cliente
    contexto = {
        'clientes': clientes
    }
    return render(request, 'listado_cliente.html', contexto)

#Agregar Cliente function
def agregar_cliente(request):
    if request.method == 'GET':
        form = ClienteForm()
        contexto = {
            'form': form
            
        }
    else:
        form = ClienteForm(request.POST)
        contexto = {
            'form': form
            
        }
        if form.is_valid():
            form.save()
            return redirect('listado_cliente')
    return render(request, 'agregar_cliente.html',contexto)




def editarCliente(request, idCliente ):
    cliente = Cliente.objects.get(idCliente = idCliente)
    if request.method == 'GET':
        form = ClienteForm(instance = cliente)
        contexto = {
            'form': form
        }
    else:
        form = ClienteForm(request.POST, instance= cliente)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('listado_cliente')

    return render(request , 'agregar_cliente.html',contexto)


def eliminarCliente(request, idCliente):
    cliente = Cliente.objects.get(idCliente=idCliente)
    cliente.delete()
    return redirect('listado_cliente')

#End Cliente





#Begin Fiado



def listado_fiado(request):
    fiados = Fiado.objects.all()   #select * from Cliente
    
    contexto = {
        'fiados': fiados
    }
    return render(request, 'listado_fiado.html', contexto)

#Agregar 
def agregar_fiado(request):
    if request.method == 'GET':
        form = FiadoForm()
        contexto = {
            'form': form
            
        }
    else:
        form = FiadoForm(request.POST)
        contexto = {
            'form': form
            
        }
        if form.is_valid():
            form.save()
            return redirect('listado_fiado')
    return render(request, 'agregar_fiado.html',contexto)




def editarFiado(request, idFiado ):
    fiado = Fiado.objects.get(idFiado = idFiado)
    if request.method == 'GET':
        form = FiadoForm(instance = fiado)
        contexto = {
            'form': form
        }
    else:
        form = FiadoForm(request.POST, instance= fiado)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('listado_fiado')

    return render(request , 'agregar_fiado.html',contexto)




#End Fiado







#Begin Producto


def listado_producto(request):
    productos = Producto.objects.all()   #select * from Producto
    contexto = {
        'productos': productos
    }
    return render(request, 'listado_producto.html', contexto)

#Agregar Cliente function
def agregar_producto(request):
    if request.method == 'GET':
        form = ProductoForm()
        contexto = {
            'form': form
            
        }
    else:
        form = ProductoForm(request.POST)
        contexto = {
            'form': form
            
        }
        if form.is_valid():
            form.save()
            messages.success("Editado")
            return redirect('listado_producto')
    return render(request, 'agregar_producto.html',contexto)




def editarProducto(request, idProducto ):
    producto = Producto.objects.get(idCliente = idProducto)
    if request.method == 'GET':
        form = ProductoForm(instance = producto)
        contexto = {
            'form': form
        }
    else:
        form = ProductoForm(request.POST, instance= producto)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('listado_producto')

    return render(request , 'agregar_producto.html',contexto)


def eliminarProducto(request, idProducto):
    producto = Producto.objects.get(idProducto=idProducto)
    producto.delete()
    return redirect('listado_producto')

#End Producto