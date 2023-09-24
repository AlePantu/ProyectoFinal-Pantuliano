from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from datetime import datetime
from .forms import PedidoFormSet

from .models import Usuario , Producto , Proveedor , Pedido
from .forms import *

# Create your views here.
def inicio(req):
    return render(req ,"inicio.html")
    
@staff_member_required(login_url='/app-store/login')
def usuarios(req):
    lista = Usuario.objects.all()

    return render(req,"usuarios.html" , {"usuarios": lista})

def productos(req):
    lista = Producto.objects.all()

    return render(req,"productos.html" , {"productos": lista})


def pedidos(req):
    pedidos = Pedido.objects.all()

    return render(req,"pedidos.html" , {"pedidos": pedidos })

@staff_member_required(login_url='/app-store/login')
def proveedores(req):
    lista = Proveedor.objects.all()

    return render(req,"proveedores.html" , {"proveedores": lista})
    


def producto_formulario(req : HttpRequest):

    print('method' , req.method)
    print('post' , req.POST)


    if req.method == 'POST':

        miFormulario = ProductoFormulario(req.POST)
        if miFormulario.is_valid():

            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            producto = Producto(nombre = data["nombre"] , tipo = data["tipo"] , modelo = data["modelo"] , descripcion = data["descripcion"])
            producto.save()
            return render (req , "inicio.html" , {"mensaje":"Producto creado con exito" })
        else:
            return render (req , "inicio.html" , {"mensaje":"Formulario Invalido" })
    else:

        miFormulario = ProductoFormulario()

        return render(req, "producto_formulario.html" , {"miFormulario" : miFormulario})
    

def proveedor_formulario(req : HttpRequest):

    print('method' , req.method)
    print('post' , req.POST)


    if req.method == 'POST':

        miFormulario = ProveedorFormulario(req.POST)
        if miFormulario.is_valid():

            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            proveedor = Proveedor(nombre = data["nombre"] , cuit = data["cuit"] , email = data["email"] , numero= data["numero"])
            proveedor.save()
            return render (req , "inicio.html" , {"mensaje":"Proveedor creado con exito" })
        else:
            return render (req , "inicio.html" , {"mensaje":"Formulario Invalido" })
    else:

        miFormulario = ProveedorFormulario()

        return render(req, "proveedor_formulario.html" , {"miFormulario" : miFormulario})
    

def busqueda_producto(req):

    return render(req, "busqueda-producto.html" )

def buscar(req):

    if req.GET["nombre"]:
        nombre = req.GET["nombre"]
        productos = Producto.objects.filter(nombre__icontains = nombre)
        if (productos.__len__() > 0):
            return render(req , "resultado-busqueda.html" ,{"productos":productos})
        else:
            return render(req , "resultado-busqueda.html" ,{"mensaje":"No se encontraron productos" })
    else:

         return HttpResponse(f'No escribiste ningun producto')


class ProductoUpdate(UpdateView):
    model = Producto
    template_name = "producto_update.html"
    fields = ("__all__")
    success_url = "/app-store/"

class ProductoDelete(DeleteView):
    model = Producto
    template_name = "producto_delete.html"
    success_url = "/app-store/"

class UsuarioDelete(DeleteView):
    model = Usuario
    template_name = "usuario_delete.html"
    success_url = "/app-store/"

class UsuarioUpdate(UpdateView):
    model = Usuario
    template_name = "usuario_update.html"
    fields = ("__all__")
    success_url = "/app-store/"

class ProveedorDelete(DeleteView):
    model = Proveedor
    template_name = "proveedor_delete.html"
    success_url = "/app-store/"

class ProveedorUpdate(UpdateView):
    model = Proveedor
    template_name = "proveedor_update.html"
    fields = ("__all__")
    success_url = "/app-store/"



class PedidoDelete(DeleteView):
    model = Pedido
    template_name = "pedido_delete.html"
    success_url = "/app-store/"

class PedidoUpdate(UpdateView):
    model = Pedido
    template_name = "pedido_update.html"
    fields = ("__all__")
    success_url = "/app-store/"



def loginView(req):

    if req.method == 'POST':

        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:
                login(req, user)
                return render(req, "inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(req, "inicio.html", {"mensaje": "Datos incorrectos"})

        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})

    else:
        miFormulario = AuthenticationForm()
        return render(req, "login.html", {"miFormulario": miFormulario})


def about(req):
    return render(req, "about.html")


def register(req):

    if req.method == 'POST':

        info = req.POST

        miFormulario = UsuarioFormulario({
            "nombre": info["nombre"],
            "apellido": info["apellido"],
            "email": info["email"],
            "nroLegajo": info["nroLegajo"]
        })
        
        userForm = UserCreationForm({
            "username": info["username"],
            "password1": info["password1"],
            "password2": info["password2"]
        })

        if miFormulario.is_valid() and userForm.is_valid():

            data = miFormulario.cleaned_data
            data.update(userForm.cleaned_data)

            user = User(username=data["username"])
            user.set_password(data["password1"])
            user.first_name=(data["nombre"])
            user.last_name =(data["apellido"])
            user.email=(data["email"])
            user.save()

            usuario = Usuario(
                nombre=data["nombre"], 
                apellido=data["apellido"], 
                email=data["email"],
                nroLegajo=data["nroLegajo"],
                user=user
            )
            usuario.save()
            return render(req, "inicio.html", {"mensaje": "Usuario creado con éxito"})
        else:
            print(miFormulario.errors)
            print(userForm.errors)
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:

        miFormulario = UsuarioFormulario()
        userForm = UserCreationForm()

        return render(req, "registro.html", {"miFormulario": miFormulario, "userForm": userForm})
    
    
def pedido_formulario(req : HttpRequest):



    if req.method == 'POST':

        miFormulario = PedidoFormSet(req.POST)
        if miFormulario.is_valid():
            
            pedido = Pedido.objects.create()
            
            for form in miFormulario:
                if form.cleaned_data.get('productos'):
                    pedido.productos.add(*form.cleaned_data['productos'])

            pedido.user = req.user
            pedido.save()
        
            return render (req , "inicio.html" , {"mensaje":"Pedido creado con exito" })
        else:
            return render (req , "inicio.html" , {"mensaje":"Formulario Invalido" })
    else:

        miFormulario = PedidoFormSet()

        return render(req, "pedido_formulario.html" , {"miFormulario" : miFormulario})