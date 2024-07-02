from django.db import models
from PIL import Image


class MainMap(models.Model):
    name = models.CharField(max_length=70, default='Main_Map')
    width = models.IntegerField(default=10)
    height = models.IntegerField(default=10)

    def __str__(self):
        return self.name

class Map(models.Model):
    main_map = models.ForeignKey(MainMap, on_delete=models.CASCADE, related_name='maps', null=True, blank=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    x_coordinate = models.IntegerField()  # Coordonnée X dans la carte générale
    y_coordinate = models.IntegerField()  # Coordonnée Y dans la carte générale
    width = models.PositiveIntegerField(default=4)
    height = models.PositiveIntegerField(default=4)

    class Meta:
        unique_together = ('main_map', 'x_coordinate', 'y_coordinate')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.generate_boxes()

    def generate_boxes(self):
        for x in range(self.width):
            for y in range(self.height):
                Box.objects.get_or_create(map=self, x_coordinate=x, y_coordinate=y)

    def __str__(self):
        return f"{self.name} ({self.x_coordinate}, {self.y_coordinate})"
    

class BoxType(models.Model):
    TYPE_CHOICES = [
        ('forest', 'Forest'),
        ('desert', 'Desert'),
        ('plain', 'plain'),
        ('mountain', 'Mountain'),
    ]
    name = models.CharField(max_length=100, choices=TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Box(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name='boxes')
    box_type = models.ForeignKey(BoxType, on_delete=models.CASCADE, null=True, blank=True)
    x_coordinate = models.IntegerField(default=0)
    y_coordinate = models.IntegerField(default=0)

    class Meta:
        unique_together = ('map', 'x_coordinate', 'y_coordinate')

    def __str__(self):
        return f"Box {self.coordinate} - {self.box_type.name if self.box_type else 'No Type'}"


class Location(models.Model):
    name = models.CharField(max_length=100)
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name='locations')
    x_coordinate = models.IntegerField()
    y_coordinate = models.IntegerField()
    
    def __str__(self):
        return self.name
    

class City(Location):
    population = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} (City)"
    

class Cave(Location):
    depth = models.IntegerField()

    def __str__(self):
        return f"{self.name} (Cave)"


class Forest(Location):

    def __str__(self):
        return f"{self.name} (Forest)"
