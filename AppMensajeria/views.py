from django.shortcuts import render
from .models import * #ImagenBlog
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import authenticate, login
from .forms import  EnviarMensajeForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.views import LogoutView
# Create your views here.
@login_required
def mensaje(request):
    if request.method=='POST':
        form=EnviarMensajeForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data()
            mensajes=mensajeria(user=request.user,Mensaje=info['Mensaje'] )
            lista=mensajeria.objects.filter(user=request.user)
            return render(request,'chat.html',{})


        pass
    else:
        mensajes=mensajeria.objects.all()
        form=EnviarMensajeForm()
        return render(request,'chat.html',{'form':form, 'mensajes':mensajes})


def enviarmensaje(request):
    if request.method=='POST':
        form=EnviarMensajeForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data()
            mensajes=Mensaje(emisor=request.user, receptor= User.id, cuerpo=info["cuerpo"])
            mensajes.save()
            pass

    else:
        form=EnviarMensajeForm()
        return render(request, 'chat.html', {'form':form})

def mostraruser(request):
    user=User.objects.all()
    return render(request,'chat.html',{'users':user})
        