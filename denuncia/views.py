from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
# Create your views here.
from .forms import *

from django.http import HttpResponse
from denuncia.models import *


def cliente_new(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
           # cliente.cedula = request.cedula
           # cliente.nombre = request.nombre
           # cliente.vehiculo = request.vehiculo
            cliente.save()
            return redirect('cliente_detail', pk=cliente.cedula)
    else:
        form = ClienteForm()
    return render(request, 'cliente/cliente_edit.html', {'form': form})

def cliente_edit(request,pk):
    cliente = get_object_or_404(Cliente, cedula=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
         #   post.author = request.user
         #   post.published_date = timezone.now()
            cliente.save()
            return redirect('cliente_detail', pk=cliente.cedula)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente/cliente_edit.html', {'form': form})    

def cliente_delete(request,pk):
    cliente = get_object_or_404(Cliente, cedula=pk)
    cliente.delete
    return redirect('cliente_list') 

def cliente_list(request):
    clientes = Cliente.objects.order_by('cedula')
    return render(request, 'cliente/cliente_list.html', {'clientes': clientes})

def cliente_detail(request,pk):
    cliente = get_object_or_404(Cliente, cedula=pk)
    return render(request, 'cliente/cliente_detail.html', {'cliente': cliente})       



def estado_new(request):
    if request.method == "POST":
        form = EstadoForm(request.POST)
        if form.is_valid():
            estado = form.save(commit=False)
           # cliente.cedula = request.cedula
           # cliente.nombre = request.nombre
           # cliente.vehiculo = request.vehiculo
            estado.save()
            return redirect('estado_detail', pk=estado.id)
    else:
        form = EstadoForm()
    return render(request, 'estado/estado_edit.html', {'form': form})

def estado_edit(request,pk):
    estado = get_object_or_404(Estado, id=pk)
    if request.method == "POST":
        form = EstadoForm(request.POST, instance=estado)
        if form.is_valid():
            estado = form.save(commit=False)
         #   post.author = request.user
         #   post.published_date = timezone.now()
            estado.save()
            return redirect('estado_detail', pk=estado.id)
    else:
        form = EstadoForm(instance=estado)
    return render(request, 'estado/estado_edit.html', {'form': form})    

def estado_delete(request,pk):
    estado = get_object_or_404(Estado, id=pk)
    estado.id
    return redirect('estado_list') 

def estado_list(request):
    estados = Estado.objects.order_by('tipo')
    return render(request, 'estado/estado_list.html', {'estados': estados})

def estado_detail(request,pk):
    estado = get_object_or_404(Estado, id=pk)
    return render(request, 'estado/estado_detail.html', {'estado': estado})   



def vehiculo_new(request):
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = form.save(commit=False)
           # cliente.cedula = request.cedula
           # cliente.nombre = request.nombre
           # cliente.vehiculo = request.vehiculo
            vehiculo.save()
            return redirect('vehiculo_detail', pk=vehiculo.matricula)
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/vehiculo_edit.html', {'form': form})

def vehiculo_edit(request,pk):
    vehiculo = get_object_or_404(Vehiculo, matricula=pk)
    if request.method == "POST":
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            vehiculo = form.save(commit=False)
         #   post.author = request.user
         #   post.published_date = timezone.now()
            vehiculo.save()
            return redirect('vehiculo_detail', pk=vehiculo.matricula)
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'vehiculo/vehiculo_edit.html', {'form': form})    

def vehiculo_delete(request,pk):
    vehiculo = get_object_or_404(Vehiculo, matricula=pk)
    vehiculo.delete
    return redirect('vehiculo_list') 

def vehiculo_list(request):
    vehiculos = Vehiculo.objects.order_by('cedula')
    return render(request, 'vehiculo/estado_list.html', {'vehiculos': vehiculos})

def vehiculo_detail(request,pk):
    vehiculo = get_object_or_404(Vehiculo, matricula=pk)
    return render(request, 'vehiculo/vehiculo_detail.html', {'vehiculo': vehiculo})     




