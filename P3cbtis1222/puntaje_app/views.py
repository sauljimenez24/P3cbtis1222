from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"index.html")
def contactos(request):
    return render(request,"contactos.html")
def empleado(request):
    return render(request,"empleado.html")

def carros(request):
    return render(request,"carros.html")
def motos(request):
    return render(request,"motos.html")
def cliente(request):
    return render(request,"cliente.html")
def provedores(request):
    return render(request,"provedores.html")