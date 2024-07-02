from django.test import TestCase

from authentication.models import User
from items.models import *
from inventory.models import InventoryItem, Inventory


class InventoryTests(TestCase):

    def setUp(self):
        """
        SetUp 1 user, and 2 Food.items for tests
        """

        self.user = User.objects.create(username='player', email='', password='password')
        self.apple = Apple.objects.create()
        self.bread = Bread.objects.create()
        

    def test_inventory_creation(self):

        # Inventory existing check
        self.assertIsNotNone(self.user.general_inventory)
        self.user.general_inventory.add_item(self.apple, 5)
        self.user.general_inventory.add_item(self.bread, 3)
        inventory_items = InventoryItem.objects.filter(inventory=self.user.general_inventory)
        apple_item = inventory_items.get(item=self.apple)
        bread_item = inventory_items.get(item=self.bread)
        self.assertEqual(apple_item.quantity, 5)
        self.assertEqual(bread_item.quantity, 3)
        print(f"{apple_item.quantity} x {apple_item.item.name} in inventory {apple_item.inventory.id}")
        print(f"{bread_item.quantity} x {bread_item.item.name} in inventory {bread_item.inventory.id}")
        
    def test_inventory_full(self):
        self.user.general_inventory.capacity = 1
        self.user.general_inventory.save()
        self.user.general_inventory.add_item(self.apple, 5)
        with self.assertRaises(ValueError):
            self.user.general_inventory.add_item(self.bread, 3)
        print(f"{self.bread} not add into inventory")

    def test_remove_item(self):
        self.user.general_inventory.add_item(self.apple, 5)
        self.user.general_inventory.add_item(self.bread, 3)
        # Vérifier que les items sont correctement ajoutés
        self.assertEqual(self.user.general_inventory.inventory_items.get(item=self.apple).quantity, 5)
        self.assertEqual(self.user.general_inventory.inventory_items.get(item=self.bread).quantity, 3)
        # Retirer des items de Food de l'inventaire de l'utilisateur
        self.user.general_inventory.remove_item(self.apple, 2)
        self.user.general_inventory.remove_item(self.bread, 3)
        self.assertEqual(self.user.general_inventory.inventory_items.get(item=self.apple).quantity, 3)
        with self.assertRaises(InventoryItem.DoesNotExist):
            self.user.general_inventory.inventory_items.get(item=self.bread)
        # Essayer de retirer plus d'items qu'il n'y en a
        with self.assertRaises(ValueError):
            self.user.general_inventory.remove_item(self.apple, 10)