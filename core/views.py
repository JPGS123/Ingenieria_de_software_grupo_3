from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Libro, Categoria, Arriendo
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.decorators import user_passes_test
from django.core.files.storage import default_storage

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser, login_url='/login/')
def usuarioAdmin(request):
    libros = Libro.objects.select_related('id_categoria').all()
    categorias = Categoria.objects.all()
    for libro in libros:
        if not libro.imagen:
            libro.imagen = 'media/imagenes/default.jpg'
    
    return render(request, 'usuario-admin.html', {'libros': libros, 'categorias': categorias})


def index(request):
    return render(request, 'index.html')

def terror(request):
    libros = Libro.objects.filter(id_categoria_id=2)
    return render(request, 'terror.html', {'libros': libros})

def cuentos(request):
    libros = Libro.objects.filter(id_categoria_id=3)
    return render(request, 'cuentos.html', {'libros': libros})

def cienciaFiccion(request):
    libros = Libro.objects.filter(id_categoria_id=1)
    return render(request, 'ciencia-ficcion.html', {'libros': libros})

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
            request.session.set_expiry(3000) 
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        telefono = request.POST.get('telefono', '').strip()
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
        
        if User.objects.filter(first_name=telefono).exists():
            messages.error(request, 'El teléfono ya está en uso.')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = telefono
        user.save()
        messages.success(request, 'Usuario registrado correctamente.')
        return redirect('login')

    return render(request, 'register.html')


@login_required
def agregar_libro(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo').strip()
        autor = request.POST.get('autor').strip()
        año_publicacion = request.POST.get('año_publicacion').strip()
        precio = request.POST.get('precio').strip()
        copias = request.POST.get('copias').strip()
        id_categoria = request.POST.get('categoria').strip()
        imagen = request.FILES.get('imagen')

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
                id_categoria=categoria,
                imagen=imagen if imagen else None
            )
            libro.save()
            return JsonResponse({'status': 'success'})
        
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Datos numéricos inválidos'}, status=400)
        
        except Categoria.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Categoría no encontrada'}, status=400)

        except Exception as e:
            print(f"Error al agregar libro: {str(e)}")
            return JsonResponse({'status': 'error', 'message': 'Ocurrió un error inesperado'}, status=500)

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

def fantasia(request):
    libros = Libro.objects.filter(id_categoria_id=4)
    return render(request, 'fantasia.html', {'libros': libros})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada con éxito')
    return redirect('index')

@login_required
def arrendar_libro(request, id_libro):
    libro = get_object_or_404(Libro, id_libro=id_libro)

    if libro.copias > 0:
        libro.copias -= 1
        libro.save()

        try:
            arriendo = Arriendo(libro=libro)
            arriendo.save()
            messages.success(request, 'Libro arrendado exitosamente.')
        except IntegrityError as e:
            print(f'Error al arrendar el libro: {str(e)}')
            messages.error(request, 'Error al arrendar el libro. Por favor, inténtelo de nuevo más tarde.')
    else:
        messages.error(request, 'No hay libros disponibles para arrendar.')

    return redirect('fantasia')


@login_required
def perfil_usuario(request):
    arriendos = Arriendo.objects.filter(libro__in=Libro.objects.all()).select_related('libro')

    libros_vistos = set()
    arriendos_unicos = []
    for arriendo in arriendos:
        if arriendo.libro.id_libro not in libros_vistos:
            libros_vistos.add(arriendo.libro.id_libro)
            arriendos_unicos.append(arriendo)

    return render(request, 'perfil.html', {'arriendos': arriendos_unicos})





