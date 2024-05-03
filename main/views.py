from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'menu.html')

def listficheros(request):
    return render(request, 'listficheros.html')

def materiaprima(request):
    pass

def fabricacion(request):
    pass

def entinvetario(request):
    pass

def escalloforma(request):
    pass

def mantficheros(request):
    pass

