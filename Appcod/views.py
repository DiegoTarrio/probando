from django.shortcuts import render
from .models import curso,familiar
from django.http import HttpResponse
# Create your views here.

def cursos(request):
    cursito=curso(Nombre="python", Comision=34645)
    cursito.save()
    cadena_de_texto=f'Curso guardado, Nombre: {cursito.nombre}, Comision: {cursito.comision}'
    return HttpResponse(cadena_de_texto)

def familiares(request):
    Padre=familiar(Nombre= 'Cristian', Nacimiento= "1970-05-18" , Edad=52)
    Madre=familiar(Nombre='Valeria', Nacimiento= "1973-07-11", Edad=49)
    Hermana=familiar(Nombre='Abril',Nacimiento= "2006-05-26" , Edad=16)
    Padre.save()
    Madre.save()
    Hermana.save()
    lista_familiares=[Padre,Madre,Hermana]
    
    return render(request,"familiar.html",{"Familiares": lista_familiares})
    
   