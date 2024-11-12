from django.shortcuts import render, get_object_or_404
from .models import Receta,Ingrediente,TipoPlato

def index(request):
    return render(request, 'index.html')

def list_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas/list.html', {'recetas': recetas})

def detail_receta(request, id):
    receta = Receta.objects.get(id=id)
    return render(request, 'recetas/detail.html', {'receta': receta})

def detail_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    ingredientes = receta.ingredientes.all()
    return render(request, 'detalles_receta.html', {'receta': receta, 'ingredientes': ingredientes})

def detail_ingrediente(request, id):
    ingrediente = Ingrediente.objects.get(id=id)
    return render(request, 'ingredientes/detail.html', {'ingrediente': ingrediente})

def list_tipos_plato(request):
    tipos_plato = TipoPlato.objects.all()
    return render(request, 'tipos_plato/list.html', {'tipos_plato': tipos_plato})

def detail_tipo_plato(request, id):
    tipo_plato = TipoPlato.objects.get(id=id)
    return render(request, 'tipos_plato/detail.html', {'tipo_plato': tipo_plato})
