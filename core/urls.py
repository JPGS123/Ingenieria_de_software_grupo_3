from django.urls import path
from .views import index, eventos, login_page, login_view, catalogo, register

urlpatterns = [
    path('', index, name='index'),
    path('eventos/', eventos, name='eventos'),
    path('login/', login_page, name='login'),
    path('login/submit/', login_view, name='login_view'),
    path('catalogo/', catalogo, name='catalogo'),
    path('register/', register, name='register'),
]