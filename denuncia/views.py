from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
# Create your views here.
from .forms import ClienteForm

from django.http import HttpResponse
from denuncia.models import Cliente


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


