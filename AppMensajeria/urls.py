from django.urls import path
from AppMensajeria.views import *

urlpatterns=[ path("chat/", enviarmensaje, name='Mensaje'),

]