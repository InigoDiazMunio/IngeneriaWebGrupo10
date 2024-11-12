
from django.test import TestCase
from .models import Receta, Ingrediente, TipoPlato

class RecetaModelTest(TestCase):
    def setUp(self):
        Receta.objects.create(nombre="Tarta de Manzana", tipo="Postre", ingredientes="Manzana, Azúcar, Harina")

    def test_receta_nombre(self):
        receta = Receta.objects.get(nombre="Tarta de Manzana")
        self.assertEqual(receta.nombre, "Tarta de Manzana")

class IngredienteModelTest(TestCase):
    def setUp(self):
        Ingrediente.objects.create(nombre="Sal", categoria="Condimento")

    def test_ingrediente_nombre(self):
        ingrediente = Ingrediente.objects.get(nombre="Sal")
        self.assertEqual(ingrediente.nombre, "Sal")

class TipoPlatoModelTest(TestCase):
    def setUp(self):
        TipoPlato.objects.create(nombre="Entrante", descripcion="Plato inicial de la comida")

    def test_tipo_plato_nombre(self):
        tipo_plato = TipoPlato.objects.get(nombre="Entrante")
        self.assertEqual(tipo_plato.nombre, "Entrante")
