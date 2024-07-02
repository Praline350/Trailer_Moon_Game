from django.contrib import admin

from trailers.models import *

@admin.register(Trailer)
class TrailerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')


@admin.register(TrailerCharacter)
class TrailerCharacterAdmin(admin.ModelAdmin):
    list_display = ('trailer', 'character')
