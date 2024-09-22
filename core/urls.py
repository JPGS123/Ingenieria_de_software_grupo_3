from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),  # Esta línea mapea la URL raíz a la vista index_view
]