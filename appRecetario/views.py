from django.shortcuts import render, get_object_or_404
from .models import Receta, Ingrediente, TipoPlato

# Vista para la página principal
def index(request):
    return render(request, 'index.html')

# Vista para listar todas las recetas
def list_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas/list.html', {'recetas': recetas})

def detail_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    ingredientes = receta.ingredientes.all()
    return render(request, 'recetas/detail.html', {'receta': receta, 'ingredientes': ingredientes})

# Vista para ver los detalles de un ingrediente específico
def detail_ingrediente(request, id):
    ingrediente = get_object_or_404(Ingrediente, id=id)
    return render(request, 'ingredientes/detail.html', {'ingrediente': ingrediente})

# Vista para listar todos los tipos de plato
def list_tipos_plato(request):
    tipos_plato = TipoPlato.objects.all()
    return render(request, 'tipos_plato/list.html', {'tipos_plato': tipos_plato})

# Vista para ver los detalles de un tipo de plato específico
def detail_tipo_plato(request, id):
    tipo_plato = get_object_or_404(TipoPlato, id=id)
    return render(request, 'tipos_plato/detail.html', {'tipo_plato': tipo_plato})
def index(request):
    tipos_plato = TipoPlato.objects.all()
    recetas = Receta.objects.all()
    ingredientes = Ingrediente.objects.all()
    return render(request, 'index.html', {
        'tipos_plato': tipos_plato,
        'recetas': recetas,
        'ingredientes': ingredientes
    })
