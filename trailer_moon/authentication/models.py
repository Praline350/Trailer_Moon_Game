from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image 

from inventory.models import *
from trailers.models import *
from locations.models import *

class User(AbstractUser):
    # AbstractUser inclut déjà les champs suivants :
    # username: CharField (unique, max_length=150)
    # first_name: CharField (max_length=150)
    # last_name: CharField (max_length=150)
    # email: EmailField (max_length=254)
    # password: CharField (haché)
    # groups: ManyToManyField (related to Group model)
    # user_permissions: ManyToManyField (related to Permission model)
    # is_staff: BooleanField (default=False)
    # is_active: BooleanField (default=True)
    # is_superuser: BooleanField (default=False)
    # last_login: DateTimeField (null=True, blank=True)
    # date_joined: DateTimeField (default=timezone.now)
    avatar = models.ImageField(null=True, blank=True, verbose_name='Avatar Image')
    general_inventory = models.OneToOneField('inventory.Inventory', on_delete=models.CASCADE, related_name='user_inventory', null=True, blank=True)
    wallet = models.BigIntegerField(default=500)
    current_map = models.ForeignKey(Map, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    x_coordinate = models.IntegerField(null=True, blank=True)
    y_coordinate = models.IntegerField(null=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.general_inventory:
            self.general_inventory = Inventory.objects.create(capacity=30)
        super().save(*args, **kwargs)
        if not hasattr(self, 'trailer'):
            Trailer.objects.create(user=self, name=f"{self}'s Trailer")

    def __str__(self):
        return self.username
