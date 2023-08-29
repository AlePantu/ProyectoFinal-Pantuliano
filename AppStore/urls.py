from django.urls import path
from .views import inicio , usuarios , productos , proveedores

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('usuarios/', usuarios ,name='Usuarios'),
    path('productos/', productos, name='Productos'),
    path('proveedores/', proveedores , name='Proveedores')
]

