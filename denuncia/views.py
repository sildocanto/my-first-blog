from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import *

#from .forms import ClienteForm

from django.http import HttpResponse
from denuncia.models import *


def cliente_new(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
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
            cliente.save()
            return redirect('cliente_detail', pk=cliente.cedula)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente/cliente_edit.html', {'form': form})    

def cliente_delete(request,pk):
    cliente = get_object_or_404(Cliente, cedula=pk)
    cliente.delete()
    return redirect('cliente_list') 

def cliente_list(request):
    clientes = Cliente.objects.order_by('cedula')
    return render(request, 'cliente/cliente_list.html', {'clientes': clientes})

def cliente_detail(request,pk):
    cliente = get_object_or_404(Cliente, cedula=pk)
    return render(request, 'cliente/cliente_detail.html', {'cliente': cliente})       


def cliente_intro(request):
    if request.method == "POST":
        form = IniClienteForm(request.POST)
        pk = request.POST.get("cedula", "")
        try:
            cliente = Cliente.objects.get(pk=pk)
            if form.is_valid():
                #return redirect('cliente_detail',pk) 
                return redirect('cliente_hayHerido',pk)      
        except Cliente.DoesNotExist:   
            return render(request, 'cliente/cliente_NoEncontrado.html',) 
    else:
        form = IniClienteForm()
    return render(request, 'cliente/cliente_intro.html', {'form': form})          
    
def cliente_hayHerido(request,pk):
    poliza = get_object_or_404(Poliza, cliente=pk)
    return render(request, 'cliente/cliente_hayHerido.html', {'poliza': poliza})

def cliente_hayTercero(request,pk):
    poliza = get_object_or_404(Poliza, nro_poliza=pk)
    return render(request, 'cliente/cliente_hayTercero.html', {'poliza': poliza})

def cliente_911(request):
    return render(request, 'cliente/911.html') 


def cliente_terceroData(request,pk):
    poliza = get_object_or_404(Poliza, nro_poliza=pk)
    if request.method == "POST":
        form = IncidenteForm(request.POST)
        if form.is_valid(): 
            incidente = form.save(commit=False)         
            incidente.save()
            return redirect('incidente_detail', pk=incidente.nro_incidente)
    else:
        form = IncidenteForm()    
    return render(request, 'cliente/cliente_terceroData.html', {'form': form})


def cliente_conductorData(request,pk):
    poliza = get_object_or_404(Poliza, nro_poliza=pk)
    if request.method == "POST":
        form = IncidenteForm(request.POST)
        if form.is_valid(): 
            incidente = form.save(commit=False)

            incidente.save() 
            return redirect('cliente_fin', pk=incidente.nro_incidente) 
           # return redirect('cliente_fin', {'form':form})
    else:
##        return render(request, 'cliente/cliente_conductorData.html', {'poliza': poliza})  
        form = IncidenteForm()     
    return render(request, 'cliente/cliente_conductorData.html', {'form': form,'poliza': poliza})             

#    poliza = get_object_or_404(Poliza, nro_poliza=pk)
 #   return render(request, 'cliente/cliente_hayTercero.html', {'poliza': poliza})

def cliente_fin(request,pk):
    incidente = get_object_or_404(Incidente, nro_incidente=pk)  
    return render(request, 'cliente/cliente_fin.html', {'incidente': incidente}) 


def estado_new(request):
    if request.method == "POST":
        form = EstadoForm(request.POST)
        if form.is_valid():
            estado = form.save(commit=False)
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
            estado.save()
            return redirect('estado_detail', pk=estado.id)
    else:
        form = EstadoForm(instance=estado)
    return render(request, 'estado/estado_edit.html', {'form': form})    

def estado_delete(request,pk):
    estado = get_object_or_404(Estado, id=pk)
    estado.delete()
    return redirect('estado_list')  

def estado_list(request):
    estados = Estado.objects.order_by('tipo')
    return render(request, 'estado/estado_list.html', {'estados': estados})

def estado_detail(request,pk):
    estado = get_object_or_404(Estado, id=pk)
    return render(request, 'estado/estado_detail.html', {'estado': estado})   


def incidente_new(request):
    if request.method == "POST":
        form = IncidenteForm(request.POST)
        if form.is_valid():
            incidente = form.save(commit=False)
            incidente.save()
            return redirect('incidente_detail', pk=incidente.nro_incidente)
    else:
        form = IncidenteForm()
    return render(request, 'incidente/incidente_edit.html', {'form': form})

def incidente_edit(request,pk):
    incidente = get_object_or_404(Incidente, nro_incidente=pk)
    if request.method == "POST":
        form = IncidenteForm(request.POST, instance=incidente)
        if form.is_valid():
            incidente = form.save(commit=False)
            incidente.save()
            return redirect('incidente_detail', pk=incidente.nro_incidente)
    else:
        form = IncidenteForm(instance=incidente)
    return render(request, 'incidente/incidente_edit.html', {'form': form})    

def incidente_delete(request,pk):
    incidente = get_object_or_404(Incidente, nro_incidente=pk)
    incidente.delete()
    return redirect('incidente_list') 

def incidente_list(request):
    incidentes = Incidente.objects.order_by('nro_incidente')
    return render(request, 'incidente/incidente_list.html', {'incidentes': incidentes})

def incidente_detail(request,pk):
    incidente = get_object_or_404(Incidente, nro_incidente=pk)
    return render(request, 'incidente/incidente_detail.html', {'incidente': incidente})      


def poliza_new(request):
    if request.method == "POST":
        form = PolizaForm(request.POST)
        if form.is_valid():
            poliza = form.save(commit=False)
            poliza.save()
            return redirect('poliza_detail', pk=poliza.nro_poliza)
    else:
        form = PolizaForm()
    return render(request, 'poliza/poliza_edit.html', {'form': form})

def poliza_edit(request,pk):
    poliza = get_object_or_404(Poliza, nro_poliza=pk)
    if request.method == "POST":
        form = PolizaForm(request.POST, instance=poliza)
        if form.is_valid():
            poliza = form.save(commit=False)
            poliza.save()
            return redirect('poliza_detail', pk=poliza.nro_poliza)
    else:
        form = PolizaForm(instance=poliza)
    return render(request, 'poliza/poliza_edit.html', {'form': form})    

def poliza_delete(request,pk):
    poliza = get_object_or_404(Poliza, nro_poliza=pk)
    poliza.delete()
    return redirect('poliza_list') 

def poliza_list(request):
    polizas = Poliza.objects.order_by('nro_poliza')
    return render(request, 'poliza/poliza_list.html', {'polizas': polizas})


def poliza_detail(request,pk):
    poliza = get_object_or_404(Poliza, nro_poliza=pk)
    return render(request, 'poliza/poliza_detail.html', {'poliza': poliza})  


def usuario_new(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
            return redirect('usuario_detail', pk=usuario.usuario_id)
    else:
        form = UsuarioForm()
    return render(request, 'usuario/usuario_edit.html', {'form': form})

def usuario_edit(request,pk):
    usuario = get_object_or_404(Usuario, usuario_id=pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
            return redirect('usuario_detail', pk=usuario.usuario_id)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuario/usuario_edit.html', {'form': form})    

def usuario_delete(request,pk):
    usuario = get_object_or_404(Usuario, usuario_id=pk)
    usuario.delete()
    return redirect('usuario_list') 

def usuario_list(request):
    usuarios = Usuario.objects.order_by('usuario_id')
    return render(request, 'usuario/usuario_list.html', {'usuarios': usuarios})

def usuario_detail(request,pk):
    usuario = get_object_or_404(Usuario, usuario_id=pk)
    return render(request, 'usuario/usuario_detail.html', {'usuario': usuario})    



def archivo_new(request):
    if request.method == "POST":
        form = ArchivoForm(request.POST)
        if form.is_valid():
            archivo = form.save(commit=False)
            archivo.save()
            return redirect('archivo_detail', pk=archivo.id)
    else:
        form = ArchivoForm()
    return render(request, 'archivo/archivo_edit.html', {'form': form})

def archivo_edit(request,pk):
    archivo = get_object_or_404(Archivo, id=pk)
    if request.method == "POST":
        form = ArchivoForm(request.POST, instance=archivo)
        if form.is_valid():
            archivo = form.save(commit=False)
            archivo.save()
            return redirect('archivo_detail', pk=archivo.id)
    else:
        form = ArchivoForm(instance=archivo)
    return render(request, 'archivo/archivo_edit.html', {'form': form})    

def archivo_delete(request,pk):
    archivo = get_object_or_404(Archivo, id=pk)
    archivo.delete()
    return redirect('archivo_list') 

def archivo_list(request):
    archivos = Archivo.objects.order_by('id')
    return render(request, 'archivo/archivo_list.html', {'archivos': archivos})

def archivo_detail(request,pk):
    archivo = get_object_or_404(Archivo, id=pk)
    return render(request, 'archivo/archivo_detail.html', {'archivo': archivo})


def comentario_new(request):
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.save()
            return redirect('comentario_detail', pk=comentario.id)
    else:
        form = ComentarioForm()
    return render(request, 'comentario/comentario_edit.html', {'form': form})

def comentario_edit(request,pk):
    comentario = get_object_or_404(Comentario, id=pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.save()
            return redirect('comentario_detail', pk=comentario.id)
    else:
        form = ComentarioForm(instance=comentario)
    return render(request, 'comentario/comentario_edit.html', {'form': form})    

def comentario_delete(request,pk):
    comentario = get_object_or_404(Comentario, id=pk)
    comentario.delete()
    return redirect('comentario_list') 

def comentario_list(request):
    comentarios = Comentario.objects.order_by('fecha')
    return render(request, 'comentario/comentario_list.html', {'comentarios': comentarios})

def comentario_detail(request,pk):
    comentario = get_object_or_404(Comentario, id=pk)
    return render(request, 'comentario/comentario_detail.html', {'comentario': comentario})


def vehiculo_new(request):
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = form.save(commit=False)
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
            vehiculo.save()
            return redirect('vehiculo_detail', pk=vehiculo.matricula)
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'vehiculo/vehiculo_edit.html', {'form': form})    

def vehiculo_delete(request,pk):
    vehiculo = get_object_or_404(Vehiculo, matricula=pk)
    vehiculo.delete()
    return redirect('vehiculo_list') 

def vehiculo_list(request):
    vehiculos = Vehiculo.objects.order_by('matricula')
    return render(request, 'vehiculo/vehiculo_list.html', {'vehiculos': vehiculos})

def vehiculo_detail(request,pk):
    vehiculo = get_object_or_404(Vehiculo, matricula=pk)
    return render(request, 'vehiculo/vehiculo_detail.html', {'vehiculo': vehiculo})  


def seguimiento_new(request):
    if request.method == "POST":
        form = IncidenteForm(request.POST)
        if form.is_valid():
            incidente = form.save(commit=False)
            incidente.save()
            return redirect('seguimiento_detail', pk=incidente.nro_incidente)
    else:
        form = IncidenteForm()
    return render(request, 'seguimiento/seguimiento_edit.html', {'form': form})

def seguimiento_edit(request,pk):
    incidente = get_object_or_404(Incidente, nro_incidente=pk)
    if request.method == "POST":
        form = IncidenteForm(request.POST, instance=incidente)
        if form.is_valid():
            incidente = form.save(commit=False)
            incidente.save()
            return redirect('seguimiento_detail', pk=incidente.nro_incidente)
    else:
        form = IncidenteForm(instance=incidente)
    return render(request, 'seguimiento/seguimiento_edit.html', {'form': form})    

def seguimiento_delete(request,pk):
    incidente = get_object_or_404(Incidente, nro_incidente=pk)
    incidente.delete()
    return redirect('seguimiento_list', {'incidente': incidente}) 

def seguimiento_list(request):
    incidentes = Incidente.objects.order_by('nro_incidente')
    return render(request, 'seguimiento/seguimiento_list.html', {'incidentes': incidentes})

def seguimiento_detail(request,pk):
    incidente = get_object_or_404(Incidente, nro_incidente=pk)
    return render(request, 'seguimiento/seguimiento_detail.html', {'incidente': incidente})      

