from django.db import models

# Create your models here.
class familiar(models.Model):
    Nombre=models.CharField(max_length=50)
    Nacimiento=models.DateField()
    Edad=models.IntegerField()
    
class Estudiante(models.Model):
    Nombre=models.CharField(max_length=50)
    Apellido=models.CharField(max_length=50)
    Email=models.EmailField()
    def __str__(self):
     return f'{self.Nombre} {self.Apellido}'

class Profesor(models.Model):
    Nombre=models.CharField(max_length=50)
    Apellido=models.CharField(max_length=50)
    Email=models.EmailField()
    Profesion=models.CharField(max_length=50)
    def __str__(self):
     return f'{self.Nombre} {self.Apellido} --{self.Profesion}'

class Entregables(models.Model):
    Nombre=models.CharField(max_length=50)
    fecha_entrega=models.DateField()
    Entregado=models.BooleanField()

class curso(models.Model):
    Nombre=models.CharField(max_length=50)
    Comision=models.IntegerField()
    def __str__(self):
     return f"{self.Nombre}"

