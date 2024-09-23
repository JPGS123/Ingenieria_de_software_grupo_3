from django.urls import path
from .views import index, eventos, login, catalogo
urlpatterns = [
    path('', index, name='index'),
    path('eventos/', eventos, name='eventos'),
    path('login/', login, name='login'),
    path('catalogo/', catalogo, name='catalogo'),
]