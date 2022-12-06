from django.shortcuts import render
from .models import curso
from django.http import HttpResponse
# Create your views here.

def curso(request):
    cursito=curso(Nombre="python", Comision=34645)
    cursito.save()
    cadena_de_texto=f'Curso guardado, Nombre: {cursito.nombre}, Comision: {cursito.comision}'
    return HttpResponse(cadena_de_texto)

def familiar(request):
    Padre=familiar(Nombre= 'Cristian', Nacimiento= '18 de mayo de 1970', Edad=52)
    Madre=familiar(Nombre='Valeria', Nacimiento='11 de julio de 1973', Edad=49)
    Hermana=familiar(Nombre='Abril',Nacimiento='26 de mayo de 2006', Edad=16)
    Padre.save()
    Madre.save()
    Hermana.save()
    lista_familiares=[Padre,Madre,Hermana]
    
    return render(request,"Appcod/familiar.html",{'Familiares': lista_familiares})
   