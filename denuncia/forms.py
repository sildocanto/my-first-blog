from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
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
