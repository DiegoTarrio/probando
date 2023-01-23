from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):
    Nombre= forms.CharField(max_length=50)
    Comision= forms.IntegerField()

class ProfeForm(forms.Form):
    nombre= forms.CharField(label="Nombre Profesor", max_length=50)
    apellido= forms.CharField(label="Apellido Profesor", max_length=50)
    email= forms.EmailField(label="Email Profesor")
    profesion= forms.CharField(label="Profesion Profesor", max_length=50)

class EstudianteForm(forms.Form):
    Nombre= forms.CharField(max_length=50)
    Apellido= forms.CharField(max_length=50)
    Email= forms.EmailField()

class BlogForm(forms.Form):
    Titulo= forms.CharField(label="titulo")
    Subtitulo= forms.CharField(label='subtitulo')
    Resu= forms.CharField(label='resumen')
    Cuerpo= forms.CharField(label='cuerpo')
    Autor= forms.CharField(label='autor')
    Fecha= forms.DateField()
    Imagen=forms.ImageField(label='imagen')



class RegiterUsuarioForm(UserCreationForm):
    email= forms.EmailField(label='Email')
    password1= forms.CharField(label='Ingrese contrasenia',widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar contrasenia',widget=forms.PasswordInput)
    first_name= forms.CharField(label='Nombre', max_length=50)

    class meta():
        model=User
        fields=['username','email','password1','password2','first_name']
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')
    
    class Meta:
        model=User
        fields=["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}#para cada uno de los campos del formulario, le asigna un valor vacio

class AvatarForm(forms.Form):
     imagen=forms.ImageField(label="Imagen")

class FotoBlogForm(forms.Form):
    imagen=forms.ImageField(label='imagen')

class EnviarMensajeForm(forms.Form):
    Cuerpo= forms.CharField(label='Ingrese un texto')