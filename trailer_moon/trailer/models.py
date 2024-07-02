from django.db import models
from django.conf import settings
from characters.models import Character

class Trailer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='trailers', null=True)
    avatar = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField(default=5)  # Capacité de colons
    water_supply = models.FloatField(default=100.0)  # Réserve d'eau
    food_supply = models.FloatField(default=100.0)  # Réserve de nourriture
    characters = models.ManyToManyField(Character, related_name='trailers', blank=True)

    def __str__(self):
        return self.name

class TrailerCharacter(models.Model):
    trailer = models.ForeignKey('trailer.Trailer', on_delete=models.CASCADE)
    character = models.ForeignKey('characters.Character', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('trailer', 'character')

    def __str__(self):
        return f"{self.character.name} in {self.trailer.name}"
