from django.contrib import admin

from trailer.models import Trailer, TrailerCharacter

@admin.register(Trailer)
class TrailerAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')

@admin.register(TrailerCharacter)
class TrailerCharacterAdmin(admin.ModelAdmin):
    list_display = ('trailer', 'character')
