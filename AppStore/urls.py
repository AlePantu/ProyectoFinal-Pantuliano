from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('usuarios/', usuarios ,name='Usuarios'),
    path('productos/', productos, name='Productos'),
    path('proveedores/', proveedores , name='Proveedores'),
    path('pedidos/', pedidos ,name='Pedidos'),
    path('producto-formulario/' , producto_formulario , name='ProductoFormulario'),
    path('pedido-formulario/' , pedido_formulario , name='PedidoFormulario'),
    path('proveedor-formulario/' , proveedor_formulario , name='ProveedorFormulario'),
    path('busqueda-producto/' , busqueda_producto , name='BusquedaProducto'),
    path('buscar/' , buscar , name='Buscar'),
    path('actualiza-producto/<pk>', ProductoUpdate.as_view(), name='ActualizarProducto'),
    path('elimina-producto/<pk>', ProductoDelete.as_view(), name='EliminaProducto'),
    path('actualiza-usuario/<pk>', UsuarioUpdate.as_view(), name='ActualizarUsuario'),
    path('elimina-usuario/<pk>', UsuarioDelete.as_view(), name='EliminaUsuario'),
    path('actualiza-proveedor/<pk>', ProveedorUpdate.as_view(), name='ActualizarProveedor'),
    path('elimina-proveedor/<pk>', ProveedorDelete.as_view(), name='EliminaProveedor'),
    path('registrar/', register, name='Registrar'),
    path('login/', loginView, name='Login'),
    path('logout/', LogoutView.as_view(template_name="inicio.html"), name="Logout"),
    path('about/', about, name='About'),
    path('actualiza-pedido/<pk>', PedidoUpdate.as_view(), name='ActualizarPedido'),
    path('elimina-pedido/<pk>', PedidoDelete.as_view(), name='EliminaPedido'),
    path('enviar-mensaje/', enviar_mensaje, name='EnviarMensaje'),
    path('ver-mensajes/', ver_mensajes, name='Mensajes'),
    path('responder-mensaje/<int:mensaje_id>/',responder_mensaje, name='responder_mensaje'),
    path('eliminar-mensaje/<pk>/', MensajeDelete.as_view(), name='EliminarMensaje'),
    path('editar-perfil/', editar_perfil, name="EditarPerfil"),
]

