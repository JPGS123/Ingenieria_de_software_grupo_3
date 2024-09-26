from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def usuarioAdmin(request):
    return render(request, 'usuario-admin.html')

def eventos(request):
    return render(request, 'eventos.html')

def login_page(request):
    return render(request, 'login.html')

def catalogo(request):
    return render(request, 'catalogo.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not email or not password:
            messages.error(request, 'Todos los campos son obligatorios.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo ya está en uso.')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Usuario registrado correctamente.')
        return redirect('login_page')

    return render(request, 'register.html')