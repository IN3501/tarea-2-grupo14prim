from django.urls import path
from .views import * 

urlpatterns = [
	path('', index, name ='index'),
	path('inputs/', inputs, name='inputs'),
	path('contacto/', contacto, name='contacto'),
	path('creacion/', creacion, name='creacion'),
	path('inicio/', inicio, name='inicio'),
	path('testimonios/', testimonios, name= 'testimonios'),
]