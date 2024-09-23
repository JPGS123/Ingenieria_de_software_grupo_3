from django.urls import path
from .views import index, eventos, login_page, catalogo, register

urlpatterns = [
    path('', index, name='index'),
    path('eventos/', eventos, name='eventos'),
    path('login/', login_page, name='login'),
    path('catalogo/', catalogo, name='catalogo'),
    path('register/', register, name='register'),
]