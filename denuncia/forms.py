from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('cedula', 'nombre','vehiculo')


class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ('id', 'tipo')


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('matricula',)