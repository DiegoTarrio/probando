from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class mensajeria(models.Model):
    Mensaje=models.CharField(max_length=50)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Mensaje(models.Model):
    Emisor=models.ForeignKey(User, on_delete=models.CASCADE)
   
    Cuerpo=models.CharField(max_length=50)
    Leido=models.BooleanField()