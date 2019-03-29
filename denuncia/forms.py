from django import forms
from denuncia.models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('cedula', 'nombre', 'vehiculo',)

class IniClienteForm(forms.Form):
    cedula = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Ej:12345678'}))
    vehiculo = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'SAA2781'}))

class TerceroDataForm(forms.Form):
    nro_poliza = forms.CharField(max_length=8)
    ter_matricula = forms.CharField(max_length=7)
    ter_aseguradora = forms.CharField(max_length=30) 
    ter_propietario = forms.BooleanField()
    ter_nombre_conductor = forms.CharField(max_length=50)
    ter_cedula_conductor = forms.CharField(max_length=8)
    ter_telefono_conductor = forms.CharField(max_length=9) 


class IncidenteForm(forms.ModelForm):
    class Meta:
        model = Incidente
        fields = ('nro_incidente', 'poliza', 'hay_heridos', 'hay_terceros', 
            'fecha_incidente', 'estado', 'pro_nombre', 'pro_cedula', 
            'pro_vto_libreta', 'pro_telefono', 'pro_email', 'pro_descripción', 
            'ter_matricula', 'ter_aseguradora', 'ter_propietario', 
            'ter_nombre_conductor', 'ter_cedula_conductor', 'ter_telefono_conductor',
             'usuario', 'fecha_mod')



class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ('id', 'tipo')


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('matricula',)


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


class SeguimientoForm(forms.ModelForm):
    class Meta:
        model = Incidente
        fields = ('nro_incidente', 'poliza', 'hay_heridos', 'hay_terceros', 'fecha_incidente', 'estado', 'pro_nombre', 'pro_cedula', 'pro_vto_libreta', 'pro_telefono', 'pro_email', 'pro_descripción', 'ter_matricula', 'ter_aseguradora', 'ter_propietario', 'ter_nombre_conductor', 'ter_cedula_conductor', 'ter_telefono_conductor', 'usuario', 'fecha_mod')


class IniSeguimientoForm(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Usuario'}))
    clave = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Clave'}), max_length=8)