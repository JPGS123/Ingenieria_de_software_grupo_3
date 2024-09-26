from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Libro
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

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

def usuarioAdmin(request):
    libros = Libro.objects.all()
    return render(request, 'usuario-admin.html', {'libros': libros})

def agregar_libro(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        año_publicacion = request.POST.get('año_publicacion')
        precio = request.POST.get('precio')
        copias = request.POST.get('copias')

        try:
            libro = Libro(titulo=titulo, autor=autor, año_publicacion=año_publicacion, precio=precio, copias=copias)
            libro.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)

def eliminar_libro(request, id_libro):
    if request.method == 'POST':
        try:
            libro = Libro.objects.get(id_libro=id_libro)
            libro.delete()
            return JsonResponse({'status': 'success'})
        except Libro.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Libro no encontrado'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)
