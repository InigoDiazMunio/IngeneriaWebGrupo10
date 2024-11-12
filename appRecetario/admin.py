
from django.contrib import admin
from .models import Receta, Ingrediente, TipoPlato

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'ingredientes')

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')

@admin.register(TipoPlato)
class TipoPlatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
