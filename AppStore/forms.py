from django import forms

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    nroLegajo = forms.IntegerField(required=True)

    
class ProductoFormulario(forms.Form):

    nombre = forms.CharField(required=True)
    tipo = forms.CharField(required=True)
    modelo = forms.CharField(required=True)
    descripcion= forms.CharField(required=True)


class ProveedorFormulario(forms.Form):

    nombre= forms.CharField(required=True)
    cuit =forms.IntegerField(required=True)
    email= forms.EmailField(required=True)
    numero = forms.IntegerField(required=True)
