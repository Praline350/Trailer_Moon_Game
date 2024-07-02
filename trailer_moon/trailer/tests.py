from django.test import TestCase
from django.contrib.auth import get_user_model
from characters.models import Character, Stats
from trailer.models import Trailer

User = get_user_model()

class TrailerCharacterTest(TestCase):

    def setUp(self):
        # Crée un utilisateur
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Crée des stats pour un personnage
        self.stats = Stats.objects.create(strength=5, agility=5, intelligence=5, social=5, perception=5, bio_connection=5)

        # Crée un personnage
        self.character = Character.objects.create(
            name='Test Character',
            age=30,
            sex='M',
            level=1,
            hp=100,
            water_necessity=1.0,
            food_necessity=1.0,
            stats=self.stats
        )

        # Crée un trailer
        self.trailer = Trailer.objects.create(
            user=self.user,
            name='Test Trailer',
            capacity=5,
            water_supply=100.0,
            food_supply=100.0
        )

    def test_assign_character_to_trailer(self):
        # Assigne le personnage au trailer
        self.trailer.characters.add(self.character)
        self.trailer.save()

        # Vérifie que le personnage est bien assigné au trailer
        self.assertIn(self.character, self.trailer.characters.all())
        self.assertEqual(self.trailer.characters.count(), 1)
        self.assertEqual(self.trailer.characters.first().name, 'Test Character')

        # Vérifie que le trailer est bien assigné au personnage
        self.assertIn(self.trailer, self.character.trailers.all())
        print(f"{self.character} est bien dans le {self.trailer}" )

