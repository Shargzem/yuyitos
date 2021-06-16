"""yuyitosProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path
from yuyitosApp.views import agregar_cliente, editarCliente, eliminarCliente, listado_cliente, inicio, agregar_producto, listado_producto, editarProducto, eliminarProducto, agregar_fiado, listado_fiado
from yuyitosApp.class_view import ClienteList, ClienteCreate, ClienteUpdate, ClienteDelete, ProductoList, ProductoCreate, ProductoUpdate, ProductoDelete, FiadoList, FiadoCreate, FiadoUpdate, FiadoDelete, Venta_detalleList, Venta_detalleCreate, Venta_detalleUpdate, Venta_detalleDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio', inicio, name='inicio'),
    path('agregar_cliente/', ClienteCreate.as_view(), name='agregar_cliente'),
    path('listado_cliente/', ClienteList.as_view(), name='listado_cliente'),
    path('editar_cliente/<int:pk>/', ClienteUpdate.as_view(), name='editar_cliente'),
    path('eliminar_cliente/<int:pk>/', ClienteDelete.as_view(), name='eliminar_cliente'),

    #Begin Producto

    path('agregar_producto/', ProductoCreate.as_view(), name='agregar_producto'),
    path('listado_producto/', ProductoList.as_view(), name='listado_producto'),
    path('editar_producto/<int:pk>/', ProductoUpdate.as_view(), name='editar_producto'),
    path('eliminar_producto/<int:pk>/', ProductoDelete.as_view(), name='eliminar_producto'),

    #End Producto


    #Begin Fiado

    path('agregar_fiado/', FiadoCreate.as_view(), name='agregar_fiado'),
    path('listado_fiado/', FiadoList.as_view(), name='listado_fiado'),
    path('editar_fiado/<int:pk>/', FiadoUpdate.as_view(), name='editar_fiado'),
    path('eliminar_fiado/<int:pk>/', FiadoDelete.as_view(), name='eliminar_fiado'),

    #End Fiado

    #Begin Venta

    path('agregar_venta/', Venta_detalleCreate.as_view(), name='agregar_venta'),
    path('listado_venta/', Venta_detalleList.as_view(), name='listado_venta'),
    path('editar_venta/<int:pk>/', Venta_detalleUpdate.as_view(), name='editar_venta'),
    path('eliminar_venta/<int:pk>/', Venta_detalleDelete.as_view(), name='eliminar_venta')

    #End Venta

]
