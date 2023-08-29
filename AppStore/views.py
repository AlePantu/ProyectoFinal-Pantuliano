from django.shortcuts import render
from .models import Usuario , Producto , Proveedor
#from django.http import HttpResponse , HttpRequest
#from .forms import CursoFormulario

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