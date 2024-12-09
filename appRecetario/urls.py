from django.urls import path, include
from django.contrib import admin
from appRecetario import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from .views import add_receta, add_ingrediente, add_tipo_plato

# Rutas envueltas en i18n_patterns para multilingüismo
urlpatterns = i18n_patterns(
    path('', views.index, name='index'),
    path('recetas/', views.list_recetas, name='list_recetas'),
    path('recetas/<int:receta_id>/', views.detail_receta, name='detail_receta'),
    path('ingredientes/', views.list_ingredientes, name='list_ingredientes'),
    path('ingredientes/<int:id>/', views.detail_ingrediente, name='detail_ingrediente'),
    path('ingredientes/<int:ingrediente_id>/recetas/', views.recetas_por_ingrediente, name='recetas_por_ingrediente'),
    path('tipos_plato/', views.list_tipos_plato, name='list_tipos_plato'),
    path('tipos_plato/<int:id>/', views.detail_tipo_plato, name='detail_tipo_plato'),
    path('contacto/', views.contacto, name='contacto'),
    path('politica-privacidad/', views.politica_privacidad, name='politica_privacidad'),
    path('terminos-condiciones/', views.terminos_condiciones, name='terminos_condiciones'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ingredientes/cargar-mas/', views.cargar_mas_ingredientes, name='cargar_mas_ingredientes'),
    path('recetas/cargar-mas/', views.cargar_mas_recetas, name='cargar_mas_recetas'),
    path('tipos-plato/cargar-mas/', views.cargar_mas_tipos_plato, name='cargar_mas_tipos_plato'),
    path('recetas/agregar/', add_receta, name='add_receta'),
    path('ingredientes/agregar/', add_ingrediente, name='add_ingrediente'),
    path('tipos-plato/agregar/', add_tipo_plato, name='add_tipo_plato'),
    path('admin/', admin.site.urls),
)

# Agregar el manejo del cambio de idioma fuera de i18n_patterns
urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),  # Ruta para cambiar el idioma
]

# Configuración para archivos estáticos y de medios
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
