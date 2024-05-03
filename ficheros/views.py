from django.shortcuts import render,redirect
from .forms import *
from main.models import *

# Create your views here.

def listcomatprima(request):
    return render(request, 'compraprima.html')

def listmatprima(request):
    return render(request, 'materiaprima.html')

def listfabricaciones(request):
    return render(request, 'fabricaciones.html')

def listformulas(request):
    return render(request, 'formulas.html')

def listformpagos(request):
    return render(request, 'formpagos.html')


