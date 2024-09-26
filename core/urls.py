from django.urls import path
from .views import index, eventos, login_page, login_view, catalogo, register, nosotros, usuarioAdmin, agregar_libro, eliminar_libro

urlpatterns = [
    path('', index, name='index'),
    path('eventos/', eventos, name='eventos'),
    path('login/', login_page, name='login'),
    path('login/submit/', login_view, name='login_view'),
    path('catalogo/', catalogo, name='catalogo'),
    path('register/', register, name='register'),
    path('nosotros/', nosotros, name='nosotros'),
    path('usuario-admin/', usuarioAdmin, name='usuario-admin'),
    path('agregar-libro/', agregar_libro, name='agregar_libro'),
    path('eliminar-libro/<int:id_libro>/', eliminar_libro, name='eliminar_libro'),
]
