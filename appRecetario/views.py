from django.shortcuts import render, get_object_or_404
from .models import Receta, Ingrediente, TipoPlato
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegisterForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import TipoPlato, Receta
from django.http import JsonResponse
from .forms import RecetaForm, IngredienteForm, TipoPlatoForm


def index(request):
    # Selecciona un tipo de plato específico, cambia el nombre si es necesario
    tipo_plato = TipoPlato.objects.filter(nombre='Ensaladas').first()

    # Verifica si el tipo de plato fue encontrado
    if not tipo_plato:
        print("Tipo de plato no encontrado.")

    recetas = Receta.objects.all()[:5]
    return render(request, 'index.html', {
        'tipo_plato': tipo_plato,
        'recetas': recetas
    })
def list_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas/list.html', {'recetas': recetas})


def detail_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    # Dividimos el texto del proceso en párrafos
    proceso_en_parrafos = receta.proceso.split('\n')
    return render(request, 'recetas/detail.html', {'receta': receta, 'proceso_parrafos': proceso_en_parrafos})
# Vista para ver los detalles de un ingrediente específico
def detail_ingrediente(request, id):
    ingrediente = get_object_or_404(Ingrediente, id=id)
    return render(request, 'ingredientes/detail.html', {'ingrediente': ingrediente})


def list_ingredientes(request):
    ingredientes = Ingrediente.objects.all()
    return render(request, 'ingredientes/list.html', {'ingredientes': ingredientes})

# Vista para listar todos los tipos de plato
def list_tipos_plato(request):
    tipos_plato = TipoPlato.objects.all()
    return render(request, 'tipos_plato/list.html', {'tipos_plato': tipos_plato})



def detail_tipo_plato(request, id):
    tipo_plato = get_object_or_404(TipoPlato, id=id)
    recetas = tipo_plato.receta_set.all()  # Obtiene las recetas asociadas al tipo de plato
    context = {
        'tipo_plato': tipo_plato,
        'recetas': recetas,
    }
    return render(request, 'tipos_plato/detail.html', context)

    
def contacto(request):
    return render(request, 'contacto.html')

def politica_privacidad(request):
    return render(request, 'politica_privacidad.html')

def terminos_condiciones(request):
    return render(request, 'terminos_condiciones.html')

# Vista para registro
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Vista para login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido, {username}')
                return redirect('index')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
        else:
            messages.error(request, 'Formulario inválido')
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# Vista para logout
def logout_view(request):
    logout(request)
    messages.info(request, 'Sesión cerrada exitosamente')
    return redirect('index')


from django.shortcuts import render, get_object_or_404
from .models import Ingrediente, Receta

def detail_ingrediente(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)
    recetas = Receta.objects.filter(ingredientes__icontains=ingrediente.nombre)
    return render(request, 'ingredientes/detail_ingrediente.html', {'ingrediente': ingrediente, 'recetas': recetas})

def recetas_por_ingrediente(request, ingrediente_id):
    ingrediente = get_object_or_404(Ingrediente, id=ingrediente_id)
    recetas = Receta.objects.filter(ingredientes__nombre__icontains=ingrediente.nombre)
    context = {
        'ingrediente': ingrediente,
        'recetas': recetas
    }
    return render(request, 'recetas_por_ingrediente.html', context)


def cargar_mas_ingredientes(request):
    offset = int(request.GET.get('offset', 0))  # Obtiene el offset actual
    limit = 10  # Define el tamaño del bloque
    ingredientes = Ingrediente.objects.all()[offset:offset + limit]  # Selecciona un rango de ingredientes

    # Prepara la respuesta en formato JSON
    data = {
        "ingredientes": [
            {
                "id": ingrediente.id,
                "nombre": ingrediente.nombre,
                "imagen": ingrediente.imagen.url if ingrediente.imagen else "",
                "categoria": ingrediente.categoria,
            }
            for ingrediente in ingredientes
        ]
    }
    return JsonResponse(data)



def list_ingredientes(request):
    # Devuelve solo los primeros 10 ingredientes
    ingredientes = Ingrediente.objects.all()[:10]
    return render(request, 'ingredientes/list.html', {'ingredientes': ingredientes})



def list_tipos_plato(request):
    # Devuelve solo los primeros 10 tipos de plato
    tipos_plato = TipoPlato.objects.all()[:10]
    return render(request, 'tipos_plato/list.html', {'tipos_plato': tipos_plato})

def list_recetas(request):
    # Devuelve solo las primeras 10 recetas
    recetas = Receta.objects.all()[:10]
    return render(request, 'recetas/list.html', {'recetas': recetas})

def cargar_mas_tipos_plato(request):
    offset = int(request.GET.get('offset', 0))
    limit = 10
    tipos_plato = TipoPlato.objects.all()[offset:offset + limit]

    data = {
        "tipos_plato": [
            {
                "id": tipo.id,
                "nombre": tipo.nombre,
                "descripcion": tipo.descripcion,
                "imagen": tipo.imagen.url if tipo.imagen else "",
            }
            for tipo in tipos_plato
        ]
    }
    return JsonResponse(data)

def cargar_mas_recetas(request):
    offset = int(request.GET.get('offset', 0))
    limit = 10
    recetas = Receta.objects.all()[offset:offset + limit]

    data = {
        "recetas": [
            {
                "id": receta.id,
                "nombre": receta.nombre,
                "imagen": receta.imagen.url if receta.imagen else "",
                "tipo_plato": receta.tipo_plato.nombre if receta.tipo_plato else "",
            }
            for receta in recetas
        ]
    }
    return JsonResponse(data)


# Vista para agregar una nueva receta
def add_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_recetas')  # Redirige a la lista de recetas
    else:
        form = RecetaForm()
    return render(request, 'recetas/form.html', {'form': form})

# Vista para agregar un nuevo ingrediente
def add_ingrediente(request):
    if request.method == 'POST':
        form = IngredienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_ingredientes')  # Redirige a la lista de ingredientes
    else:
        form = IngredienteForm()
    return render(request, 'ingredientes/form.html', {'form': form})

# Vista para agregar un nuevo tipo de plato
def add_tipo_plato(request):
    if request.method == 'POST':
        form = TipoPlatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_tipos_plato')  # Redirige a la lista de tipos de plato
    else:
        form = TipoPlatoForm()
    return render(request, 'tipos_plato/form.html', {'form': form})
