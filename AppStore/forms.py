from django import forms
from django.contrib.auth.forms import UserChangeForm ,UserCreationForm
from django.forms import formset_factory
from django.contrib.auth.models import User
from .models import *

class UsuarioFormulario(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ('nombre','apellido', 'email', 'nroLegajo')

    

    
class ProductoFormulario(forms.Form):

    nombre = forms.CharField(required=True)
    tipo = forms.CharField(required=True)
    modelo = forms.CharField(required=True)
    descripcion= forms.CharField(required=True)
    stock =forms.IntegerField(required=True)


class ProveedorFormulario(forms.Form):

    nombre= forms.CharField(required=True)
    cuit =forms.IntegerField(required=True)
    email= forms.EmailField(required=True)
    numero = forms.IntegerField(required=True)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        #help_texts = {k:"" for k in fields}


class PedidoFormulario(forms.Form):
    
   productos = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

PedidoFormSet = formset_factory(PedidoFormulario)


class MensajeForm(forms.ModelForm):
    destinatario = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Destinatario'
    )

    class Meta:
        model = Mensaje
        fields = ['destinatario', 'contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu mensaje...'}),
        }