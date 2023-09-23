from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Usuario , Producto , Proveedor
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

@staff_member_required(login_url='/app-store/login')
def proveedores(req):
    lista = Proveedor.objects.all()

    return render(req,"proveedores.html" , {"proveedores": lista})


def usuario_formulario(req : HttpRequest):

    print('method' , req.method)
    print('post' , req.POST)


    if req.method == 'POST':

        miFormulario = UsuarioFormulario(req.POST)
        if miFormulario.is_valid():

            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            usuario = Usuario(nombre = data["nombre"] , apellido = data["apellido"] , email = data["email"] , nroLegajo = data["nroLegajo"])
            usuario.save()
            return render (req , "inicio.html" , {"mensaje":"Usuario creado con exito" })
        else:
            return render (req , "inicio.html" , {"mensaje":"Formulario Invalido" })
    else:

        miFormulario = UsuarioFormulario()

        return render(req, "usuario_formulario.html" , {"miFormulario" : miFormulario})
    


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
        print('aca'+nombre)
        productos = Producto.objects.filter(nombre__icontains = nombre)
        if productos:
            return render(req , "resultado-busqueda.html" ,{"productos":productos})
    else:

         return HttpResponse(f'No escribiste ningun producto')


class ProductoUpdate(UpdateView):
    model = Producto
    template_name = "producto_update.html"
    fields = ("__all__")
    success_url = "/app-coder/"

class ProductoDelete(DeleteView):
    model = Producto
    template_name = "producto_delete.html"
    success_url = "/app-coder/"

class UsuarioDelete(DeleteView):
    model = Usuario
    template_name = "usuario_delete.html"
    success_url = "/app-coder/"

class UsuarioUpdate(UpdateView):
    model = Usuario
    template_name = "usuario_update.html"
    fields = ("__all__")
    success_url = "/app-coder/"

class ProveedorDelete(DeleteView):
    model = Proveedor
    template_name = "proveedor_delete.html"
    success_url = "/app-coder/"

class ProveedorUpdate(UpdateView):
    model = Proveedor
    template_name = "proveedor_update.html"
    fields = ("__all__")
    success_url = "/app-coder/"



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

def register(req):

    if req.method == 'POST':

        miFormulario = UserRegisterForm(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario = data["username"]

            miFormulario.save()
            print("TRUE")
            return render(req, "inicio.html", {"mensaje": f"Usuario {usuario} creado con éxito!"})

        else:
            print("FALSE")
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
        
    else:
        print("NO POST")
        miFormulario = UserRegisterForm()
        return render(req, "registro.html", {"miFormulario": miFormulario})


def about(req):
    return render(req, "about.html")