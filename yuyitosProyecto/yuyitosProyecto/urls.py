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
from yuyitosApp.views import agregar_cliente, editarCliente, eliminarCliente, listado_cliente, inicio
from yuyitosApp.class_view import ClienteList, ClienteCreate, ClienteUpdate, ClienteDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio', inicio, name='inicio'),
    path('agregar_cliente/', ClienteCreate.as_view(), name='agregar_cliente'),
    path('listado_cliente/', ClienteList.as_view(), name='listado_cliente'),
    path('editar_cliente/<int:pk>/', ClienteUpdate.as_view(), name='editar_cliente'),
    path('eliminar_cliente/<int:pk>/', ClienteDelete.as_view(), name='eliminar_cliente')
]
