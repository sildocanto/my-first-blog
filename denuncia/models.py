from django.db import models
from django.utils import timezone


class Vehiculo(models.Model):
    matricula = models.CharField(primary_key=True, max_length=7)
    cedula = models.ForeignKey('Cliente',on_delete=models.CASCADE,max_length=8)
    nombre = models.CharField(max_length=30)


    def __str__(self):
        return self.matricula 
 
class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=10)

    def __str__(self):
        return self.tipo 

class Cliente(models.Model):
    cedula = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=30)
    vehiculo = models.ForeignKey('Vehiculo',on_delete=models.CASCADE,)

    def __str__(self):
        return self.cedula


class Usuario(models.Model):
    usuario_id  = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    usuario = models.CharField(max_length=8)   
    clave = models.CharField(max_length=8)

    def __str__(self):
        return self.nombre 

class Poliza(models.Model):
    nro_poliza = models.CharField(primary_key=True, max_length=8)
    cliente = models.ForeignKey('Cliente',on_delete=models.CASCADE,)
    vehiculo = models.ForeignKey('Vehiculo',on_delete=models.CASCADE,)

    def __str__(self):
        return self.nro_poliza


class Incidente(models.Model):
    nro_incidente = models.AutoField(primary_key=True)
    poliza = models.ForeignKey('Poliza',on_delete=models.CASCADE,) 
    hay_heridos = models.BooleanField()
    hay_terceros = models.BooleanField()
    fehca_incidente = models.DateTimeField(default=timezone.now)
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

    def publish(self):
        self.fecha_mod = timezone.now()
        self.save()

    def __str__(self):
        return self.pro_nombre +' '+ self.pro_cedula


class Archivo(models.Model):
    id = models.AutoField(primary_key=True)
    incidente = models.ForeignKey('Incidente',on_delete=models.CASCADE,)
    link = models.CharField(max_length=200) 

    def __str__(self):
        return self.link 

class Comentarios(models.Model):
    id = models.AutoField(primary_key=True)
    incidente = models.ForeignKey('Incidente',on_delete=models.CASCADE,)
    comentarios = models.TextField(max_length=400)    
    fecha =  models.DateTimeField(default=timezone.now)   
    usuario = models.CharField(max_length=8)    
    unidad_org = models.CharField(max_length=25)



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.unidad_org


