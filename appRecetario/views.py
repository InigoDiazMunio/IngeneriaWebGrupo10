from django.shortcuts import render, get_object_or_404
from .models import Receta, Ingrediente, TipoPlato
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegisterForm
# Vista para la página principal
def index(request):
    # Selecciona una receta destacada, por ejemplo, la primera receta.
    plato_destacado = Receta.objects.first()  
    return render(request, 'index.html', {
        'plato_destacado': plato_destacado,
    })
    
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


def list_ingredientes(request):
    ingredientes = Ingrediente.objects.all()
    return render(request, 'ingredientes/list.html', {'ingredientes': ingredientes})

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
