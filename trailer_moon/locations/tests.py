from django.test import TestCase

from locations.models import *


class LocationTests(TestCase):
    def setUp(self):
        self.main_map = Map.objects.create(name='Main Map', description='The main World', width=8, height=8)
        self.city = City.objects.create(name='Townsville', map=self.main_map, x_coordinate=10, y_coordinate=20, population=5000)
        self.cave= Cave.objects.create(name='Dark Cave', map=self.main_map, x_coordinate=15, y_coordinate=25, depth=5)
        self.forest = Forest.objects.create(name='Mystic Forest', map=self.main_map, x_coordinate=20, y_coordinate=30)
        self.forest_type = BoxType.objects.create(name='Forest', description='A dense forest')
        self.plain_type = BoxType.objects.create(name='Plain', description='A wide open plain')
        boxes = self.main_map.boxes.all()
        for box in boxes:
            if (ord(box.coordinate[0]) + int(box.coordinate[1])) % 2 == 0:
                box.box_type = self.forest_type
            else:
                box.box_type = self.plain_type
            box.save()

    def test_create_locations(self):
        self.assertIsNotNone(self.city.id)
        self.assertIsNotNone(self.cave.id)
        self.assertIsNotNone(self.forest.id)


    def test_create_boxes(self):
        # Vérifier que les cases ont été créées correctement
        boxes = self.main_map.boxes.all()
        self.assertEqual(len(boxes), 64)  # 8x8 grille doit avoir 64 cases

        for x in range(self.main_map.width):
            for y in range(self.main_map.height):
                coordinate = f"{chr(65 + x)}{y + 1}"  # Générer des coordonnées comme 'A1', 'B2', etc.
                box = boxes.get(coordinate=coordinate)
                self.assertIsNotNone(box)
                # Vérifier le type de la case
                expected_type = self.forest_type if (ord(coordinate[0]) + int(coordinate[1])) % 2 == 0 else self.plain_type
                self.assertEqual(box.box_type, expected_type)

    def test_box_coordinates(self):
        # Vérifier que chaque case a des coordonnées correctes
        boxes = self.main_map.boxes.all()
        for box in boxes:
            coordinate = box.coordinate
            self.assertTrue(coordinate[0].isalpha())
            self.assertTrue(coordinate[1:].isdigit())
            x = ord(coordinate[0]) - 65
            y = int(coordinate[1:]) - 1
            self.assertTrue(0 <= x < self.main_map.width)
            self.assertTrue(0 <= y < self.main_map.height)