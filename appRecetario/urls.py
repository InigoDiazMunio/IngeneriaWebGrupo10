from django.urls import path, include
from django.contrib import admin
from appRecetario import views

urlpatterns = [
    path('', views.list_recetas, name='index'),
    path('recetas/', views.list_recetas, name='list_recetas'),
    path('recetas/<int:receta_id>/', views.detail_receta, name='detail_receta'),
    path('ingredientes/', views.list_ingredientes, name='list_ingredientes'),
    path('ingredientes/<int:id>/', views.detail_ingrediente, name='detail_ingrediente'),
    path('tipos_plato/', views.list_tipos_plato, name='list_tipos_plato'),
    path('tipos_plato/<int:id>/', views.detail_tipo_plato, name='detail_tipo_plato'),
    path('contacto/', views.contacto, name='contacto'),
]
