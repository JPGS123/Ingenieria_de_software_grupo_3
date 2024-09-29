from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Libro, Categoria
from django.http import JsonResponse
from django.contrib.auth import logout



def index(request):
    return render(request, 'index.html')

def perfil(request):
    return render(request, 'perfil.html')

def fantasia(request):
    return render(request, 'fantasia.html')

def terror(request):
    return render(request, 'terror.html')

def cuentos(request):
    return render(request, 'cuentos.html')

def cienciaFiccion(request):
    return render(request, 'ciencia-ficcion.html')

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
        return redirect('login')

    return render(request, 'register.html')

def usuarioAdmin(request):
    libros = Libro.objects.select_related('id_categoria').all()
    categorias = Categoria.objects.all()
    return render(request, 'usuario-admin.html', {'libros': libros, 'categorias': categorias})


def agregar_libro(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        año_publicacion = request.POST.get('año_publicacion')
        precio = request.POST.get('precio')
        copias = request.POST.get('copias')
        id_categoria = request.POST.get('categoria')
        if not titulo or not autor or not año_publicacion or not precio or not copias or not id_categoria:
            return JsonResponse({'status': 'error', 'message': 'Todos los campos son obligatorios'}, status=400)
        try:
            año_publicacion = int(año_publicacion)
            copias = int(copias)
            precio = float(precio)
            categoria = Categoria.objects.get(id_categoria=id_categoria)
            
            libro = Libro(
                titulo=titulo,
                autor=autor,
                año_publicacion=año_publicacion,
                precio=precio,
                copias=copias,
                id_categoria=categoria
            )
            libro.save()
            return JsonResponse({'status': 'success'})
        except ValueError as ve:
            return JsonResponse({'status': 'error', 'message': 'Datos numéricos inválidos'}, status=400)
        except Categoria.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Categoría no encontrada'}, status=400)
        except Exception as e:
            print(f"Error al agregar libro: {str(e)}")
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

def editar_libro(request, id_libro):
    if request.method == 'POST':
        try:
            libro_id = request.POST.get('libro_id')
            titulo = request.POST.get('titulo')
            autor = request.POST.get('autor')
            año_publicacion = request.POST.get('año_publicacion')
            precio = request.POST.get('precio')
            copias = request.POST.get('copias')
            id_categoria = request.POST.get('categoria')

            print(f"Libro ID: {libro_id}")
            print(f"Título: {titulo}")
            print(f"Autor: {autor}")
            print(f"Año de Publicación: {año_publicacion}")
            print(f"Precio: {precio}")
            print(f"Copias: {copias}")
            print(f"ID Categoría: {id_categoria}")

            libro = Libro.objects.get(id_libro=libro_id)
            categoria = Categoria.objects.get(id_categoria=id_categoria)
            
            libro.titulo = titulo
            libro.autor = autor
            libro.año_publicacion = año_publicacion
            libro.precio = precio
            libro.copias = copias
            libro.id_categoria = categoria

            libro.save()
            return JsonResponse({'status': 'success'})

        except Exception as e:
            print(f"Error: {str(e)}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/lista.html', {'categorias': categorias})

def agregar_categoria(request):
    if request.method == 'POST':
        nombre_categoria = request.POST.get('nombre_categoria')
        Categoria.objects.create(nombre_categoria=nombre_categoria)
        return redirect('lista_categorias')
    return render(request, 'categorias/agregar.html')

def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        categoria.nombre_categoria = request.POST.get('nombre_categoria')
        categoria.save()
        return redirect('lista_categorias')
    return render(request, 'categorias/editar.html', {'categoria': categoria})

def eliminar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('lista_categorias')

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada con éxito')
    return redirect('index')
