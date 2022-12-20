from django.urls import path
from Appcod.views import *

urlpatterns = [
    path('familiar/',familiares),
    path('curso',cursito),
    path('cursos/',leercursos,name='Cursos'),
    path('entregables/',entregables,name='Entregables'),
    path('estudiantes/',estudiantes,name='Estudiantes'),
    path('profesores/',leerProfesores,name='Profesores'),
    path('',inicio,name='Inicio'),
    path('padre/',padre,name='Padre'),

    path('cursoformulario/',cursoformulario,name='CursoFormulario'),
    path("profeFormulario/", profeFormulario, name="profeFormulario"),
    path("busquedaComision/", busquedaComision, name="busquedaComision"),
    path("buscar/", buscar, name="buscar"),

    path("leerProfesores/", leerProfesores, name="leerProfesores"),
    path("eliminarProfesor/<id>", eliminarProfesor, name="eliminarProfesor"),
    path("editarProfesor/<id>", editarProfesor, name="editarProfesor"),
    path('buscarprofesores/', buscarprofesor, name="buscarProfesores"),

    path('leercursos/',leercursos, name="LeerCursos"),
    path('eliminarcurso/<id>', eliminarcurso, name="EliminarCurso"),
    path('editarcurso/<id>', editarcurso, name="EditarCurso"),

    path('eliminarestudiante/<id>',eliminarestudiante, name='EliminarEstudiante'),
    path('editarestudiante/<id>', editarestudiante, name='EditarEstudiante'),
    path('estudianteformulario/', estudianteformulario, name="EstudianteFormulario"),
    path('buscarestudiante/', buscarestudiante, name='buscarEstudiante'),

    
]