from ssl import HAS_TLSv1_1
from turtle import title
from unicodedata import numeric
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from inventario.forms import productoForm

from .models import producto
from .forms import *

def home(request):
    return render(request, 'home.html')



def inv(request):
    searchTerm= request.GET.get('buscarProducto')
    if searchTerm:
        Productos = producto.objects.filter(Nombre__icontains=searchTerm)
    else:
        Productos=producto.objects.all()
    return render(request, 'inv.html', {'searchTerm':searchTerm, 'Productos':Productos})


def crearProducto(request, *args, **kwargs):
    if request.method == 'POST':
        form = productoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/inventario/') 
        else:
            messages.error(request, form.errors)
    else:
        form = productoForm()

    context = {'form': form, 'disabled': (kwargs.get('pk', None) != None)}

    return render(request, 'crearProducto.html', context) 


def actualizarProducto(request,pk):
    instance = get_object_or_404(producto, id=pk)

    if request.method == 'POST':
        form = productoForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            return redirect('/inventario/') 
    else:
        form = productoForm(instance=instance)

    context={'form': form}
    return render(request, 'crearProducto.html', context) 

def venderProducto(request,pk):
    instance = get_object_or_404(producto, id=pk)
    if request.method == "POST":
        numero=producto.objects.get(id=pk)
        if numero.Cantidad > 0:
            numero.Cantidad-=1
            numero.save()
            messages.success(request, 'Producto Vendido Exitosamente!')
            return redirect('/inventario/')
        else:
            messages.error(request, 'No tiene más producto disponible para vender')
            return redirect('/inventario/')
    context={'producto': instance}
    return render(request,'vender.html', context) 