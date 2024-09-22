from django.urls import path
from .views import index, eventos

urlpatterns = [
    path('', index, name='index'),
    path('eventos/', eventos, name='eventos'),
]