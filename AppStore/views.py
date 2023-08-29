from django.shortcuts import render
from .models import Usuario , Producto , Proveedor
from django.http import HttpResponse , HttpRequest
from .forms import *

# Create your views here.
def inicio(req):
    return render(req ,"inicio.html")
    

def usuarios(req):
    lista = Usuario.objects.all()

    return render(req,"usuarios.html" , {"usuarios": lista})

def productos(req):
    lista = Producto.objects.all()

    return render(req,"productos.html" , {"productos": lista})

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