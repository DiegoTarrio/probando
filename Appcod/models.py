from django.db import models
from django.contrib.auth.models import User

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

class Blog(models.Model):
    Titulo=models.CharField(max_length=50)
    Subtitulo=models.CharField(max_length=50)
    Resu=models.CharField(max_length=50)
    Cuerpo=models.CharField(max_length=50)
    Autor=models.CharField(max_length=50)
    Fecha=models.DateField()
    Imagen=models.ImageField(upload_to="blog")

    

class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)

#class ImagenBlog(models.Model):
 #   Imagen=models.ImageField(upload_to="blog")
  #  blog=models.ForeignKey(Blog, on_delete=models.CASCADE)
class Mensaje(models.Model):
    Emisor=models.ForeignKey(User, on_delete=models.CASCADE)
    
    Cuerpo=models.CharField(max_length=50)
    Leido=models.BooleanField()