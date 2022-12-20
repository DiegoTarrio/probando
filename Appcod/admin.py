from django.contrib import admin
from .models import curso, Profesor,Estudiante,Entregables
# Register your models here.

admin.site.register(curso)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Entregables)