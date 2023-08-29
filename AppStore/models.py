from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    nroLegajo = models.IntegerField(max_length=4)

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido} , legajo nro:{self.nroLegajo}'
    
class Producto(models.Model):

    nombreProd = models.CharField(max_length=30)
    tipoProd = models.CharField(max_length=30)
    modeloProd = models.CharField(max_length=30)
    descripProd = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.nombreProd}, tipo producto: {self.tipoProd} , modelo: {self.nroLegajo} , descripcion: {self.descripProd}'

class Proveedor(models.Model):

    nombreProv = models.CharField(max_length=30)
    cuitProv =models.IntegerField(max_length=11)
    emailProv = models.EmailField(null=True)
    nroProv = models.IntegerField(max_length=4)

    def __str__(self) -> str:
        return f'{self.nombreProv} , CUIT:  {self.cuitProv} , nro Proveedor: {self.nroProv} , email: {self.emailProv}'