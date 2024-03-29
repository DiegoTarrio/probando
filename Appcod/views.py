from django.shortcuts import render
from .models import curso,familiar,Profesor, Estudiante, Avatar, Blog #ImagenBlog
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import CursoFormulario, ProfeForm, EstudianteForm,RegiterUsuarioForm,UserEditForm, AvatarForm,BlogForm, FotoBlogForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.views import LogoutView
# Create your views here.

def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar=""
    return avatar

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
    blogs=Blog.objects.all()
    return render(request,"index.html",{'blogs':blogs})
@login_required
def profesores(request):
    blogs=Blog.objects.all()
    return render(request,'profesores.html', {'blogs':blogs})
@login_required    
def estudiantes(request):
    estudiante= Estudiante.objects.all()   
    return render(request,'estudiantes.html', {"estudiantes":estudiante, 'avatar':obtenerAvatar(request)})
@login_required    
def cursos(request):
    return render(request,'cursos.html')
@login_required    
def entregables(request):
    return render(request,'entregables.html')
def padre(request):
    return render(request,'padre.html')
@login_required
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
@login_required        
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
@login_required
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

@login_required
def eliminarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    print(profesor)
    profesor.delete()
    profesores=Profesor.objects.all()
    return render(request, "profesores.html", {"profesores": profesores, "mensaje": "Profesor eliminado correctamente"})

@login_required
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

#def mostrarblog(request):
 #   blogs=blog.objects.all()
  #  return render(request,'blog.html',{'blogs':blogs})

def register(request):
    if request.method=="POST":
        form=RegiterUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            return render(request,'index.html',{'mensaje':'Usuario creado correctamente'})

        else:
            return render(request,'register.html',{'form':form, 'mensaje':"error al crear el usuario"})

    else:
        form=RegiterUsuarioForm()
        return render(request,'register.html',{'form':form})

'''
def login_request(request):
    if request.method=='POST':
        form=AuthenticationForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info['username']
            clave=info['password']
            usuario=authenticate(username=usu, password=clave) #verifica si el usuario existe
            if usuario is not None:
                login(request,usuario)
                return render(request,'index.html', {'mensaje':'Usuario {usu} logueado correctamente'})
            else:
                return render(request, 'login.html',{'form':form ,'mensaje':'Usuario o Contrasenia incorrectoss'})
        else:
            return render(request, 'login.html',{'form':form ,'mensaje':'Usuario o Contrasenia incorrectos'})
            

    else:
        form=AuthenticationForm()
        return render(request,'login.html',{'form':form}) '''

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)#verifica si el usuario existe, si existe, lo devuelve, y si no devuelve None 
            if usuario is not None:
                login(request, usuario)
                return render(request, "index.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "login.html", {"form": form})

@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "index.html", {"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "editarperfil.html", {"form": form, "nombreusuario":usuario.username})
    else:
        
        form=UserEditForm(initial={'email':usuario.email,'first_name':usuario.first_name, 'last_name':usuario.last_name})
        return render(request, "editarperfil.html", {"form": form, "nombreusuario":usuario.username})

def agregaravatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST,request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request,'index.html',{'mensaje':'avatar agregado correctamente'})
        else:
            return render(request,'agregaravatar.html',{'form':form, 'mensaje':'algo fallo' })
    else:
        form=AvatarForm()
        return render(request,'agregaravatar.html',{'form':form, 'usuario':request.user})

def agregarblog(request):
    if request.method == 'POST':
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid():
            Titulo=form.cleaned_data.get('Titulo')
            Subtitulo=form.cleaned_data.get('Subtitulo')
            Resu=form.cleaned_data.get('Resu')
            Cuerpo=form.cleaned_data.get('Cuerpo')
            Autor=form.cleaned_data.get('Autor')
            Fecha=form.cleaned_data.get('Fecha')
            Imagen=request.FILES['Imagen']
            print(Titulo,Subtitulo,Resu,Cuerpo,Autor,Fecha,Imagen)
            blog=Blog(Titulo=Titulo, Subtitulo=Subtitulo, Resu=Resu, Cuerpo=Cuerpo, Autor=Autor, Fecha=Fecha, Imagen=Imagen)
            blog.save()
            blogs=Blog.objects.all()

            #blog=Blog(Titulo=info['Titulo'],Subtitulo=info['Subtitulo'],Resu=info['Resu'],Cuerpo=info['Cuerpo'],Autor=request.user,Fecha=info['Fecha'])
        
            return render(request,'index.html',{'blogs':blogs})
        else:
            return render(request,'agregarblog.html', {'form':form,'mensaje':'ha ocurrido un error'})
    else:
        form=BlogForm()
        return render(request,'agregarblog.html',{'form':form})

def fotoblog(request):
    if request.method=="POST":
        form=FotoBlogForm(request.POST,request.FILES)
        if form.is_valid():
            avatar=ImagenBlog(blog=request.blog, imagen=request.FILES["imagen"])
            avatarViejo=ImagenBlog.objects.filter(Blog=request.blog)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request,'index.html',{'mensaje':'avatar agregado correctamente'})
        else:
            return render(request,'agregarblog.html',{'forms':form, 'mensaje':'algo fallo' })
    else:
        return FotoBlogForm()


        

