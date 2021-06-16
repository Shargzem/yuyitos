from django.db import models
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView #View
from django.urls import reverse_lazy
from .forms import FiadoForm, ClienteForm, ProductoForm, VentaForm
from .models import Fiado, Cliente, Producto, Venta_detalle
from django.contrib import messages

#Begin Cliente

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


#End Cliente


#Begin Producto


class ProductoList(ListView):
    model = Producto
    template_name = 'listado_producto.html'

    #def get_queryset(self): 
     #   return self.model.objects.all()[:2]

class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'agregar_producto.html'
    success_url = reverse_lazy('listado_producto')

class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'agregar_producto.html'
    success_url = reverse_lazy('listado_producto')
    

class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'confirmar.html'
    success_url = reverse_lazy('listado_producto')





#Begin Fiado


class FiadoList(ListView):
    model = Fiado
    template_name = 'listado_fiado.html'

    #def get_queryset(self): 
     #   return self.model.objects.all()[:2]

class FiadoCreate(CreateView):
    model = Fiado
    form_class = FiadoForm
    template_name = 'agregar_fiado.html'
    success_url = reverse_lazy('listado_fiado')

class FiadoUpdate(UpdateView):
    model = Fiado
    form_class = FiadoForm
    template_name = 'agregar_fiado.html'
    success_url = reverse_lazy('listado_fiado')
    

class FiadoDelete(DeleteView):
    model = Fiado
    template_name = 'confirmar.html'
    success_url = reverse_lazy('listado_fiado')


#End Fiado



#Begin venta_detalle

class Venta_detalleList(ListView):
    model = Venta_detalle
    template_name = 'listado_venta.html'

    #def get_queryset(self): 
     #   return self.model.objects.all()[:2]

class Venta_detalleCreate(CreateView):
    model = Venta_detalle
    form_class = VentaForm
    template_name = 'agregar_venta.html'
    success_url = reverse_lazy('listado_venta')

class Venta_detalleUpdate(UpdateView):
    model = Venta_detalle
    form_class = VentaForm
    template_name = 'agregar_venta.html'
    success_url = reverse_lazy('listado_venta')
    

class Venta_detalleDelete(DeleteView):
    model = Venta_detalle
    template_name = 'confirmar.html'
    success_url = reverse_lazy('listado_venta')


#End venta_detalle