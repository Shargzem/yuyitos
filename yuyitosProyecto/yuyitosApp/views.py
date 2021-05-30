from django.http import request
from django.shortcuts import redirect, render
from .models import Cliente
from .forms import ClienteForm

# Create your views here.

#se envia data como un diccionario(contexto)

def inicio(request):
    return render(request, 'inicio.html')


def listado_cliente(request):
    clientes = Cliente.objects.all()   #select * from Cliente
    contexto = {
        'clientes': clientes
    }
    return render(request, 'listado_cliente.html', contexto)


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
