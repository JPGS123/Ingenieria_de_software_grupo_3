from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def eventos(request):
    return render(request, 'eventos.html')
