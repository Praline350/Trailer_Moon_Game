from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    value = models.PositiveIntegerField(default=1)
    
    class Meta: 
        abstract = False

    def __str__(self):
        return self.name


# Pour créer des objets spécifique, faire hérité une classe de la Superclass Item


class Food(Item):
    health_value = models.IntegerField()
    expiration_date = models.DateField(null=True, blank=True)

    def set_defaults(self, defaults):
        for attr, value in defaults.items():
            if not getattr(self, attr):
                setattr(self, attr, value)

    def __str__(self):
        return super().__str__()
    

class Apple(Food):
    
    def save(self, *args, **kwargs):
        self.set_defaults({
            'name': 'Apple',
            'description': 'A delicious, refreshing apple',
            'health_value': 5,
            'value': 3,
        })
        super().save(*args, **kwargs)
    
    def __str__(self):
        return super().__str__()
    

class Bread(Food):
    
    def save(self, *args, **kwargs):
        self.set_defaults({
            'name': 'Bread',
            'description': 'Classic, but nutritious',
            'health_value': 15,
            'value': 6,
        })
        super().save(*args, **kwargs)

    
    def __str__(self):
        return super().__str__()
    

        


    