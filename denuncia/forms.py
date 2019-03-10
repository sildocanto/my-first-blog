from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
<<<<<<< HEAD
        fields = ('cedula', 'nombre','vehiculo',)

class IniClienteForm(forms.Form):
	cedula = forms.CharField(max_length=100)


class XIniClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = [
			'cedula',
			'vehiculo',
		]
		labels = {
			'cedula': 'Cedula',
			'vehiculo':'Matricula',
		}
		widgets = {
			'cedula': forms.TextInput(attrs={'class':'form-control'}),
			'matricula': forms.TextInput(attrs={'class':'form-control'}),
		}
=======
        fields = ('cedula', 'nombre', 'vehiculo')


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
        fields = ('nro_incidente','poliza','hay_heridos','hay_terceros','fecha_incidente','estado','pro_nombre','pro_cedula','pro_vto_libreta','pro_telefono','pro_email','pro_descripción','ter_matricula','ter_aseguradora','ter_propietario','ter_nombre_conductor','ter_cedula_conductor','ter_telefono_conductor','usuario','fecha_mod')


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
>>>>>>> eed97789f87c7b6aa94e8eac792c8d2f8cd9f672
