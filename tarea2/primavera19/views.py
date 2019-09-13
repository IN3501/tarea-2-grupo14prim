from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'home.html')

def inputs(request):
	return render(request, 'inputs.html')

def inicio(request):
	return render(request, 'inicio.html')

def creacion(request):
	return render(request, 'creacion.html')

def contacto(request):
	return render(request, 'contacto.html')		

def testimonios(request):
	return render(request, 'testimonios.html')		