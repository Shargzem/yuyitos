from django.shortcuts import render
from .models import Cliente

# Create your views here.

#se envia data como un diccionario(contexto)


def agregar_cliente(request):
    clientes = Cliente.objects.all()   #select * from Cliente
    contexto = {
        'clientes': clientes
    }
    return render(request, 'cliente.html', contexto)