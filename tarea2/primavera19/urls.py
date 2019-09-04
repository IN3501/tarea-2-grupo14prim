from django.urls import path
from .views import * 

urlpatterns = [
	path('', index, name ='index'),
	path('inputs/', inputs, name='inputs'),
	path('formulario1/', formulario1, name='formulario1'),
	path('formulario2/', formulario2, name='formulario2'),
	path('formulario3/', formulario3, name='formulario3'),
]