from django.test import TestCase
from django.contrib.auth import get_user_model

User= get_user_model()


class UserTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Player', password='password')

    def test_create_user(self):
        # Vérifie que l'utilisateur a été créé
        self.assertIsNotNone(self.user.id)

        # Vérifie les attributs de l'utilisateur
        self.assertEqual(self.user.username, 'Player')
        self.assertTrue(self.user.check_password('password'))

        # Vérifie que l'utilisateur n'est pas un superutilisateur ni un staff
        self.assertFalse(self.user.is_superuser)
        self.assertFalse(self.user.is_staff)
        self.assertTrue(hasattr(self.user, 'trailers'))
        self.assertEqual(self.user.trailers.count(), 1)
