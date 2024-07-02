from django.contrib import admin

from locations.models import *


@admin.register(MainMap)
class MainMapAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'x_coordinate', 'y_coordinate')
