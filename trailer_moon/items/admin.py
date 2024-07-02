from django.contrib import admin

from items.models import Item, Food

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'health_value',)
