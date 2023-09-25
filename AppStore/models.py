from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(null=True)
    nroLegajo = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE , null=True)

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido} , legajo nro:{self.nroLegajo}'
    
class Producto(models.Model):

    nombre = models.CharField(max_length=50)
    tipo= models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    descripcion= models.CharField(max_length=150)
    stock = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.nombre}, tipo producto: {self.tipo} , modelo: {self.modelo} , descripcion: {self.descripcion}'

class Proveedor(models.Model):

    nombre = models.CharField(max_length=30)
    cuit =models.IntegerField()
    email = models.EmailField(null=True)
    numero = models.IntegerField()
    def __str__(self) -> str:
        return f'{self.nombre} , CUIT:  {self.cuit} , nro Proveedor: {self.numero} , email: {self.email}'
    
class Pedido(models.Model):

    fecha = models.DateField(auto_now_add=True)
    productos = models.ManyToManyField(Producto)
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True)

    def __str__(self) -> str:
        return f'Fecha :{self.fecha} , Productos:  {self.productos} , Usuario: {self.user}'
    

class Mensaje(models.Model):
    emisor = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'De {self.emisor} a {self.receptor} ({self.fecha_envio})'