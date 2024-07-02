from django.test import TestCase
from characters.models import Character, Stats

class CharacterCreationTest(TestCase):

    def setUp(self):
        # Crée des stats pour un personnage
        self.stats = Stats.objects.create(
            strength=5,
            agility=5,
            intelligence=5,
            social=5,
            perception=5,
            bio_connection=5
        )

    def test_create_character(self):
        # Crée un personnage
        character = Character.objects.create(
            name='Test Character',
            age=30,
            sex='M',
            level=1,
            hp=100,
            water_necessity=1.0,
            food_necessity=1.0,
            stats=self.stats
        )

        # Vérifie que le personnage a été créé correctement
        self.assertEqual(character.name, 'Test Character')
        self.assertEqual(character.age, 30)
        self.assertEqual(character.sex, 'M')
        self.assertEqual(character.level, 1)
        self.assertEqual(character.hp, 100)
        self.assertEqual(character.water_necessity, 1.0)
        self.assertEqual(character.food_necessity, 1.0)
        self.assertEqual(character.stats.strength, 5)
        self.assertEqual(character.stats.agility, 5)
        self.assertEqual(character.stats.intelligence, 5)
        self.assertEqual(character.stats.social, 5)
        self.assertEqual(character.stats.perception, 5)
        self.assertEqual(character.stats.bio_connection, 5)
