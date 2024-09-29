from django.urls import path
from .views import usuarioAdmin, index, eventos, login_page, login_view, catalogo, register, nosotros, usuarioAdmin, agregar_libro, eliminar_libro, editar_libro, cienciaFiccion, fantasia, terror, cuentos, lista_categorias, agregar_categoria, editar_categoria, eliminar_categoria, logout_view, perfil

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('eventos/', eventos, name='eventos'),
    path('login/', login_page, name='login'),
    path('login/submit/', login_view, name='login_view'),
    path('catalogo/', catalogo, name='catalogo'),
    path('register/', register, name='register'),
    path('nosotros/', nosotros, name='nosotros'),
    path('usuario-admin/', usuarioAdmin, name='usuario-admin'),
    path('agregar-libro/', agregar_libro, name='agregar_libro'),
    path('eliminar-libro/<int:id_libro>/', eliminar_libro, name='eliminar_libro'),
    path('editar-libro/', editar_libro, name='editar_libro'),
    path('ciencia-ficcion/', cienciaFiccion, name='ciencia-ficcion'),
    path('fantasia/', fantasia, name='fantasia'),
    path('terror/', terror, name='terror'),
    path('cuentos/', cuentos, name='cuentos'),
    path('categorias/', lista_categorias, name='lista_categorias'),
    path('categorias/agregar/', agregar_categoria, name='agregar_categoria'),
    path('editar-libro/<int:id_libro>/', editar_libro, name='editar_libro'),
    path('categorias/eliminar/<int:id>/', eliminar_categoria, name='eliminar_categoria'),
    path('logout/', logout_view, name='logout'),
    path('perfil/', perfil, name='perfil'),
]