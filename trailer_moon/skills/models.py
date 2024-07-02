from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    level_required = models.IntegerField(default=1)

    def __str__(self):
        return self.name

