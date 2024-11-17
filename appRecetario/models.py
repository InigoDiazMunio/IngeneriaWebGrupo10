from django.db import models
from django.utils import timezone

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='ingredientes/', blank=True, null=True)

    def __str__(self):
        return self.nombre


class TipoPlato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='tipoPlato/', blank=True, null=True)
    def __str__(self):
        return self.nombre

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_plato = models.ForeignKey('TipoPlato', on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField('Ingrediente')  # Cambiado a ManyToManyField
    imagen = models.ImageField(upload_to='recetas/', blank=True, null=True)

    def __str__(self):
        return self.nombre


class Inspiracion(models.Model):
    tipo_plato = models.ForeignKey('TipoPlato', on_delete=models.SET_NULL, null=True)
    fecha_actualizacion = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Inspiración: {self.tipo_plato.nombre if self.tipo_plato else 'Sin Plato'}"