from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Receta, Ingrediente, TipoPlato

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Formulario para registro de usuario
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Formulario para crear y actualizar Recetas
class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['nombre', 'tipo_plato', 'ingredientes', 'imagen']
        widgets = {
            'ingredientes': forms.CheckboxSelectMultiple,  # Para seleccionar múltiples ingredientes
        }

# Formulario para crear y actualizar Ingredientes
class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nombre', 'categoria', 'descripcion', 'imagen']

# Formulario para crear y actualizar Tipos de Plato
class TipoPlatoForm(forms.ModelForm):
    class Meta:
        model = TipoPlato
        fields = ['nombre', 'descripcion', 'imagen']