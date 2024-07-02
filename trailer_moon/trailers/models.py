from django.db import models
from django.conf import settings
from characters.models import Character

class Trailer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='trailers', null=True)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField(default=5)  # Capacité de colons
    water_supply = models.FloatField(default=100.0)  # Réserve d'eau
    food_supply = models.FloatField(default=100.0)  # Réserve de nourriture
    characters = models.ManyToManyField(Character, related_name='trailers', blank=True, through='TrailerCharacter')

    def __str__(self):
        return self.name

    def add_character(self, character):
        if self.characters.count() >= self.capacity:
            raise ValueError("Trailer is full")
        TrailerCharacter.objects.create(trailer=self, character=character)

    def remove_character(self, character):
        try:
            trailer_character = TrailerCharacter.objects.get(trailer=self, character=character)
            trailer_character.delete()
        except:
            raise ValueError("Character not found")


class TrailerCharacter(models.Model):
    trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('trailer', 'character')

    def __str__(self):
        return f"{self.character.name} in {self.trailer.name}"