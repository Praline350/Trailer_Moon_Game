from django.contrib import admin

from inventory.models import Inventory, InventoryItem

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'capacity', 'display_items')

    def user_name(self, obj):
        return f"{obj.user_inventory.username}'s Inventory"
    
    

    def display_items(self, obj):
        items = obj.items.all()
        return ", ".join([item.name for item in items])

    display_items.short_description = 'Items in Inventory'
    
@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display  = ('inventory', 'item')