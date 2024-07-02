from django.test import TestCase
from authentication.models import User
from characters.models import Character, Stats
from trailers.models import Trailer, TrailerCharacter


class TrailerTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='player', email='player@example.com', password='password')
        self.trailer = Trailer.objects.create(user=self.user, name='Main Trailer', capacity=2)
        self.character1 = Character.objects.create(name='John', age=30, sex='M')
        self.character2 = Character.objects.create(name='Jane', age=28, sex='F')
        self.character3 = Character.objects.create(name='Bob', age=35, sex='M')


    def test_add_character_to_trailer(self):
        self.trailer.add_character(self.character1)
        self.assertEqual(self.trailer.characters.count(), 1)
        # Ajouter un deuxième personnage
        self.trailer.add_character(self.character2)
        self.assertEqual(self.trailer.characters.count(), 2)
        # Tenter d'ajouter un troisième personnage (devrait échouer)
        with self.assertRaises(ValueError):
            self.trailer.add_character(self.character3)


    def test_remove_character_from_trailer(self):
        # Ajouter et ensuite supprimer un personnage
        self.trailer.add_character(self.character1)
        self.assertEqual(self.trailer.characters.count(), 1)
        # Supprimer le personnage
        self.trailer.remove_character(self.character1)
        self.assertEqual(self.trailer.characters.count(), 0)
        # Essayer de supprimer un personnage qui n'est pas dans le trailer (devrait échouer)
        with self.assertRaises(ValueError):
            self.trailer.remove_character(self.character2)