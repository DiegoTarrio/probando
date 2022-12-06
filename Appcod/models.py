from django.db import models

# Create your models here.
class familiar(models.Model):
    Nombre=models.CharField(max_length=50)
    Nacimiento=models.DateField()
    Edad=models.IntegerField()
    
class estudiante(models.Model):
    Nombre=models.CharField(max_length=50)
    Apellido=models.CharField(max_length=50)
    Email=models.EmailField()

class profesor(models.Model):
    Nombre=models.CharField(max_length=50)
    Apellido=models.CharField(max_length=50)
    Email=models.EmailField()
    Profesion=models.CharField(max_length=50)

class entregables(models.Model):
    Nombre=models.CharField(max_length=50)
    fecha_entrega=models.DateField()
    Entregado=models.BooleanField()

class curso(models.Model):
    Nombre=models.CharField(max_length=50)
    Comision=models.IntegerField()

