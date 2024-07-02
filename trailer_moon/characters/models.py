from django.db import models
from PIL import Image
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]


class Stats(models.Model):
    strength = models.IntegerField(default=1)
    agility = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    social = models.IntegerField(default=1)
    perception = models.IntegerField(default=1)
    bio_connection = models.IntegerField(default=1)

    def __str__(self):
        return f"Stats: STR={self.strength}, AGI={self.agility}, INT={self.intelligence}, SOC={self.social}, PER={self.perception}, BIO={self.bio_connection}"


class Character(models.Model):
    avatar = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    level = models.IntegerField(default=1)
    hp = models.IntegerField(default=100)
    water_necessity = models.FloatField(default=1.0)  # Quantité d'eau nécessaire par jour
    food_necessity = models.FloatField(default=1.0)  # Quantité de nourriture nécessaire par jour
    stats = models.OneToOneField(Stats, on_delete=models.CASCADE, related_name='character', null=True, blank=True)
    skills = models.ManyToManyField('skills.Skill', through='characters.CharacterSkill', blank=True)
    stuff = models.ManyToManyField('items.Item', through='characters.CharacterItem', blank=True)

    def save(self, *args, **kwargs):
        if not self.stats:
            self.stats = Stats.objects.create()
        Trailer
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class CharacterSkill(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    skill = models.ForeignKey('skills.Skill', on_delete=models.CASCADE)
    proficiency = models.IntegerField(default=0)  # Niveau de compétence

    class Meta:
        unique_together = ('character', 'skill')

    def __str__(self):
        return f"{self.character.name} - {self.skill.name} (Proficiency: {self.proficiency})"


class CharacterItem(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    item = models.ForeignKey('items.Item', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)  # Quantité d'objets

    class Meta:
        unique_together = ('character', 'item')

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"