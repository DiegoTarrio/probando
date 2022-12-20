from django.shortcuts import render
from .models import curso,familiar,Profesor, Estudiante
from django.http import HttpResponse
from .forms import CursoFormulario, ProfeForm, EstudianteForm
# Create your views here.

def cursito(request):
    cursito1=curso(Nombre="python", Comision=34645)
    cursito1.save()
    cadena_de_texto=f'Curso guardado, Nombre: {cursito1.Nombre}, Comision: {cursito1.Comision}'
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
    
def inicio(request):
    return render(request,"index.html")
def profesores(request):
    return render(request,'profesores.html')
def estudiantes(request):
    estudiante= Estudiante.objects.all()
    return render(request,'estudiantes.html', {"estudiantes":estudiante})
def cursos(request):
    return render(request,'cursos.html')
def entregables(request):
    return render(request,'entregables.html')
def padre(request):
    return render(request,'padre.html')

def cursoformulario(request):
    if request.method == 'POST':
        miFormulario=CursoFormulario(request.POST) #llega toda la informacion del html
        print(miFormulario)

        if miFormulario.is_valid:

            informacion=miFormulario.cleaned_data
            cuurso= curso(Nombre=informacion['Nombre'], Comision=informacion['Comision'])
            cuurso.save()
            todos=curso.objects.all()

            return render(request,'cursos.html', {"cursos": todos})
    else:
        miFormulario=CursoFormulario()

    return render(request,'cursoformulario.html', {"miFormulario": miFormulario})

#def buscar(request):
    if request.get['Comision']:
        comision=request.get['Comision']
        cuurso=curso.objects.filter(Comision_icontains=comision)

        return render(request,'resultadosBusqueda.html', {"cursos":cuurso, "camada":comision})

    else:
        respuesta='no enviaste datos'
        HttpResponse(respuesta)
def profeFormulario(request):
    if request.method=="POST":
        form= ProfeForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            nombre= informacion["nombre"]
            apellido= informacion["apellido"]
            email= informacion["email"]
            profesion= informacion["profesion"]
            profe= Profesor(Nombre=nombre, Apellido=apellido, Email=email, Profesion=profesion)
            profe.save()
            profesores=Profesor.objects.all()
            return render(request, "profesores.html" ,{"profesores":profesores, "mensaje": "Profesor guardado correctamente"})
        else:
            return render(request, "profeformulario.html" ,{"form": form, "mensaje": "Informacion no valida"})
        
    else:
        formulario= ProfeForm()
        return render(request,'profeformulario.html', {'form':formulario})

def busquedaComision(request):
    return render(request, "busquedacomision.html")

def buscar(request):
    
    comision= request.GET["Comision"]
    if comision!="":
        cursos= curso.objects.filter(Comision__icontains=comision)#buscar otros filtros en la documentacion de django
        return render(request, "resultadosBusqueda.html", {"cursos": cursos})
    else:
        return render(request, "busquedaComision.html", {"mensaje": "Che Ingresa una comision para buscar!"})


def leerProfesores(request):
    profesores=Profesor.objects.all()
    return render(request, "profesores.html", {"profesores": profesores})


def eliminarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    print(profesor)
    profesor.delete()
    profesores=Profesor.objects.all()
    return render(request, "profesores.html", {"profesores": profesores, "mensaje": "Profesor eliminado correctamente"})


def editarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    if request.method=="POST":
        form= ProfeForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            profesor.Nombre=info["nombre"]
            profesor.Apellido=info["apellido"]
            profesor.Email=info["email"]
            profesor.Profesion=info["profesion"]
            profesor.save()
            profesores=Profesor.objects.all()
            return render(request, "profesores.html" ,{"profesores":profesores, "mensaje": "Profesor editado correctamente"})   
    else:
        formulario= ProfeForm(initial={"nombre":profesor.Nombre, "apellido":profesor.Apellido, "email":profesor.Email, "profesion":profesor.Profesion})
        return render(request, "editarprofesor.html", {"form": formulario, "profesor": profesor})


def leercursos(request):
    cursos=curso.objects.all()
    return render(request, 'cursos.html', {"cursos":cursos})

def eliminarcurso(request, id):
    cursito=curso.objects.get(id=id)
    cursito.delete()
    cursos=curso.objects.all()
    return render(request, 'cursos.html',{"cursos":cursos})

def editarcurso(request, id):
    cursito=curso.objects.get(id=id)
    if request.method=="POST":
          form=CursoFormulario(request.POST)
          if form.is_valid():
            info=form.cleaned_data
            cursito.Nombre=info['Nombre']
            cursito.Comision=info['Comision']
            cursito.save()
            cursos=curso.objects.all()
            return render(request, "cursos.html", {'cursos':cursos})
    else:
        formulario=CursoFormulario(initial={'Nombre':cursito.Nombre, 'Comision':cursito.Comision})
    return render(request,'editarcurso.html',{"form":formulario, "curso":cursito})


def eliminarestudiante(request, id):
    estudiante=Estudiante.objects.get(id=id)
    estudiante.delete()
    estudiante=Estudiante.objects.all()
    return render(request,'estudiantes.html', {"estudiantes":estudiante})

def editarestudiante(request, id):
    estudiante=Estudiante.objects.get(id=id)
    if request.method== 'POST':
        form=EstudianteForm(request.POST)
        if form.is_valid():
           info=form.cleaned_data
           estudiante.Nombre=info['Nombre']
           estudiante.Apellido=info['Apellido']
           estudiante.Email=info['Email']
           estudiante.save()
           estudiante=Estudiante.objects.all()
           return render(request, 'estudiantes.html', {'estudiantes':estudiante})

        pass
    else:
        form=EstudianteForm(initial={'Nombre':estudiante.Nombre, 'Apellido':estudiante.Apellido, 'Email':estudiante.Email})
        return render(request,'editarestudiante.html', {'form': form, "estudiante":estudiante})

def estudianteformulario(request):
    if request.method=="POST":
        form=EstudianteForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info['Nombre']
            apellido=info['Apellido']
            email=info['Email']
            estudiante=Estudiante(Nombre=nombre, Apellido=apellido, Email=email)
            estudiante.save()
            estudiantes=Estudiante.objects.all()
            return render(request, 'estudiantes.html', {'estudiantes':estudiantes})
        
    else:
        form=EstudianteForm()
        return render(request, 'estudianteformulario.html', {"form":form})

#../assets/img/bg-masthead.jpg


def buscarestudiante(request):
    
    nombre= request.GET["nombre"]
    if nombre!="":
        estudiante= Estudiante.objects.filter(Nombre__icontains=nombre)#buscar otros filtros en la documentacion de django
        return render(request, "busquedaestudiante.html", {"estudiantes": estudiante})
    else:
        return render(request, "estudiantes.html", {"mensaje": "Che Ingresa una comision para buscar!"})


def buscarprofesor(request):
    
    nombre= request.GET["nombre"]
    if nombre!="":
        profesor= Profesor.objects.filter(Nombre__icontains=nombre)#buscar otros filtros en la documentacion de django
        return render(request, "busquedaprofesor.html", {"profesores": profesor})
    else:
        return render(request, "profesores.html", {"mensaje": "Che Ingresa una comision para buscar!"})