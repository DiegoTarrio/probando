from django.http import HttpResponse
import datetime
from django.template import Template, context, loader
def saludar(request):
    return HttpResponse ('hola mundo')
def dia_dehoy(request):
    dia=datetime.datetime.today()
    cadena='hoy es {dia}'
    return HttpResponse(cadena)
def saludo_con_nombre(request,nombre):
    return HttpResponse(f'hola {nombre} como estas')
def calcular_edad(request,edad):
    anioactual=datetime.datetime.today().year
    edad_actual=anioactual-int(edad)
    return HttpResponse(f'<h1>Tu anio de nacimiento es {edad_actual}</h1>')
'''def probandohtml(request):
    ruta=open('C:/Users/abril/PythonProyecto1/Proyecto1/plantilla/template1.html')
    template=Template(ruta.read()) #el template es la forma en q yo lo muestro
    ruta.close()
    contexto=context() #sirve para mandar datos a la planilla
    documento=template.render(contexto) #llena los espacios vacios(del html q esta en planilla) con lo que indique el context
    return HttpResponse(documento)'''
def probandohtml(request):
    diccionario={'Nombre': 'Diego', 'Apellido': 'Tarrio', 'Edad': '18', 'Lista_de_notas':[4,5,8,8,9,7]}
    template= loader.get_template('template1.html')
    documento= template.render(diccionario)
    return HttpResponse(documento)