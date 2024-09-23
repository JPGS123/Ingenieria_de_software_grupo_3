from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def eventos(request):
    return render(request, 'eventos.html')

def login(request):
    return render(request, 'login.html')

def catalogo(request):
    return render(request, 'catalogo.html')