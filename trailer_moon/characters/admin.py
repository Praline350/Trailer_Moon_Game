from django.contrib import admin
from characters.models import Character, Stats

# Utilise le décorateur `@admin.register` correctement
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    search_fields = ('name',)
    list_filter = ('sex', 'level')
    exclude = ('stats',)

@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    list_display = ('character', 'strength', 'agility', 'intelligence', 'social', 'perception', 'bio_connection')
