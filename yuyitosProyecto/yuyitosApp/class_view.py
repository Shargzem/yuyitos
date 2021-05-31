from django.db import models
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView #View
from django.urls import reverse_lazy
from .forms import ClienteForm
from .models import Cliente


class ClienteList(ListView):
    model = Cliente
    template_name = 'listado_cliente.html'

    #def get_queryset(self): 
     #   return self.model.objects.all()[:2]

class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'agregar_cliente.html'
    success_url = reverse_lazy('listado_cliente')

class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'agregar_cliente.html'
    success_url = reverse_lazy('listado_cliente')

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'confirmar.html'
    success_url = reverse_lazy('listado_cliente')