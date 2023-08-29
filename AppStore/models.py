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

    nombre = models.CharField(max_length=30)
    tipo= models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    descripcion= models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.nombre}, tipo producto: {self.tipo} , modelo: {self.modelo} , descripcion: {self.descripcion}'

class Proveedor(models.Model):

    nombre = models.CharField(max_length=30)
    cuit =models.IntegerField(max_length=11)
    email = models.EmailField(null=True)
    numero = models.IntegerField(max_length=4)

    def __str__(self) -> str:
        return f'{self.nombre} , CUIT:  {self.cuit} , nro Proveedor: {self.numero} , email: {self.email}'