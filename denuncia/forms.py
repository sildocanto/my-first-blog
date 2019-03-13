from django import forms
from denuncia.models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('cedula', 'nombre', 'vehiculo',)

class IniClienteForm(forms.Form):
	cedula = forms.CharField(max_length=100)


class TerceroDataForm(forms.Form):
    ter_matricula = forms.CharField(max_length=7)
    ter_aseguradora = forms.CharField(max_length=30) 
    ter_propietario = forms.BooleanField()
    ter_nombre_conductor = forms.CharField(max_length=30)
    ter_cedula_conductor = forms.CharField(max_length=8)
    ter_telefono_conductor = forms.CharField(max_length=9) 



class Xxx__Incidente(forms.ModelForm):
    nro_incidente = models.AutoField(primary_key=True)
    poliza = models.ForeignKey('Poliza',on_delete=models.CASCADE,) 
    hay_heridos = models.BooleanField()
    hay_terceros = models.BooleanField()
    fecha_incidente = models.DateTimeField(default=timezone.now)
    estado = models.ForeignKey('Estado',on_delete=models.CASCADE,)
    pro_nombre = models.CharField(max_length=30)
    pro_cedula = models.CharField(max_length=8)
    pro_vto_libreta = models.DateField(null=True, blank=True) 
    pro_telefono = models.CharField(max_length=9) 
    pro_email = models.EmailField(max_length=35, null=True, blank=True) 
    pro_descripción = models.TextField(max_length=500) 
    ter_matricula = models.CharField(max_length=7, null=True, blank=True)
    ter_aseguradora = models.CharField(max_length=30, null=True, blank=True) 
    ter_propietario = models.BooleanField()
    ter_nombre_conductor = models.CharField(max_length=30, null=True, blank=True)
    ter_cedula_conductor = models.CharField(max_length=8, null=True, blank=True)
    ter_telefono_conductor = models.CharField(max_length=9, null=True, blank=True) 
    usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE,)
    fecha_mod = models.DateTimeField(default=timezone.now)





class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ('id', 'tipo')


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('matricula',)


class IncidenteForm(forms.ModelForm):
    class Meta:
        model = Incidente
        fields = ('nro_incidente', 'poliza', 'hay_heridos', 'hay_terceros', 'fecha_incidente', 'estado', 'pro_nombre', 'pro_cedula', 'pro_vto_libreta', 'pro_telefono', 'pro_email', 'pro_descripción', 'ter_matricula', 'ter_aseguradora', 'ter_propietario', 'ter_nombre_conductor', 'ter_cedula_conductor', 'ter_telefono_conductor', 'usuario', 'fecha_mod')


class PolizaForm(forms.ModelForm):
    class Meta:
        model = Poliza
        fields = ('nro_poliza', 'cliente', 'vehiculo')


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('usuario_id', 'nombre', 'usuario', 'clave')


class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ('id', 'incidente', 'link')


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('id', 'incidente', 'comentario', 'fecha', 'usuario', 'unidad_org')