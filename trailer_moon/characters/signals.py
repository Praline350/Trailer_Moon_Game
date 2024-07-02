from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Character, Stats

@receiver(post_save, sender=Character)
def create_default_stats(sender, instance, created, **kwargs):
    if created and instance.stats is None:
        stats = Stats.objects.create(
            strength=1,
            agility=1,
            intelligence=1,
            social=1,
            perception=1,
            bio_connection=1
        )
        instance.stats = stats
        instance.save()