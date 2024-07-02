from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image 

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

    def __str__(self):
        return self.username
