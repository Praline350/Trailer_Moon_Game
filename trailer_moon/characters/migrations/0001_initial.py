# Generated by Django 5.0.6 on 2024-06-26 14:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
        ('skills', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strength', models.IntegerField(default=1)),
                ('agility', models.IntegerField(default=1)),
                ('intelligence', models.IntegerField(default=1)),
                ('social', models.IntegerField(default=1)),
                ('perception', models.IntegerField(default=1)),
                ('bio_connection', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('level', models.IntegerField(default=1)),
                ('hp', models.IntegerField(default=100)),
                ('water_necessity', models.FloatField(default=1.0)),
                ('food_necessity', models.FloatField(default=1.0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.character')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
            ],
            options={
                'unique_together': {('character', 'item')},
            },
        ),
        migrations.AddField(
            model_name='character',
            name='stuff',
            field=models.ManyToManyField(through='characters.CharacterItem', to='items.item'),
        ),
        migrations.CreateModel(
            name='CharacterSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proficiency', models.IntegerField(default=0)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.character')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skills.skill')),
            ],
            options={
                'unique_together': {('character', 'skill')},
            },
        ),
        migrations.AddField(
            model_name='character',
            name='skills',
            field=models.ManyToManyField(through='characters.CharacterSkill', to='skills.skill'),
        ),
        migrations.AddField(
            model_name='character',
            name='stats',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='character', to='characters.stats'),
        ),
    ]
