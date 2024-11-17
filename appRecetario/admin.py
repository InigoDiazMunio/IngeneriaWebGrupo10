
from django.contrib import admin
from .models import Receta, Ingrediente, TipoPlato

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'mostrar_ingredientes']

    def mostrar_ingredientes(self, obj):
        return ", ".join([ingrediente.nombre for ingrediente in obj.ingredientes.all()])

    mostrar_ingredientes.short_description = 'Ingredientes'

# Registro de Ingrediente
@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')

# Registro de TipoPlato
@admin.register(TipoPlato)
class TipoPlatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')


