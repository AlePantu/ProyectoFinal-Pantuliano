from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('usuarios/', usuarios ,name='Usuarios'),
    path('productos/', productos, name='Productos'),
    path('proveedores/', proveedores , name='Proveedores'),
    path('usuario-formulario/' , usuario_formulario , name='UsuarioFormulario'),
    path('producto-formulario/' , producto_formulario , name='ProductoFormulario'),
    path('proveedor-formulario/' , proveedor_formulario , name='ProveedorFormulario')
]

