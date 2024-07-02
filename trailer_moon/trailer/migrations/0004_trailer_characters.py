# Generated by Django 5.0.6 on 2024-06-26 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0005_remove_character_user'),
        ('trailer', '0003_trailer_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='trailer',
            name='characters',
            field=models.ManyToManyField(blank=True, related_name='trailers', to='characters.character'),
        ),
    ]
