from django.test import TestCase

from items.models import *

class ItemTests(TestCase):
    
    def setUp(self):
        self.apple = Apple.objects.create()
        self.bread = Bread.objects.create()

    def test_create_items(self):

        # Vérifier que les instances ont été créées et existent dans la base de données
        self.assertIsNotNone(self.apple.id)
        self.assertIsNotNone(self.bread.id)
        # Vérifier les valeurs par défaut de l'instance Apple
        self.assertEqual(self.apple.name, "Apple")
        self.assertEqual(self.apple.description, "A delicious, refreshing apple")
        self.assertEqual(self.apple.health_value, 5)
        # Vérifier les valeurs par défaut de l'instance Bread
        self.assertEqual(self.bread.name, "Bread")
        self.assertEqual(self.bread.description, "Classic, but nutritious")
        self.assertEqual(self.bread.health_value, 15)
        # Optionnel : afficher les instances créées pour la vérification manuelle
        print(self.apple)
        print(self.bread)