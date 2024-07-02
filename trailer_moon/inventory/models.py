from django.db import models

class Inventory(models.Model):
    capacity = models.PositiveIntegerField(default=20)
    items = models.ManyToManyField('items.Item', through='inventory.InventoryItem')

    def __str__(self):
        # Assure-toi que l'utilisateur est lié à cet inventaire
        user = self.user_inventory if hasattr(self, 'user_inventory') else None
        return f"Inventory of {user.username if user else 'No User'}"
    
    def add_item(self, item, quantity):
        if self.inventory_items.count() >= self.capacity:
            raise ValueError('Inventory Full')
        InventoryItem.objects.create(inventory=self, item=item, quantity=quantity)

    def remove_item(self, item, quantity):
        try:
            inventory_item = self.inventory_items.get(item=item)
            if inventory_item.quantity < quantity:
                raise ValueError('Not enought items to remove')
            inventory_item.quantity -= quantity
            if inventory_item.quantity == 0:
                inventory_item.delete()
            else: 
                inventory_item.save()
        except:
            raise ValueError('Item not found')
    

class InventoryItem(models.Model):
    inventory = models.ForeignKey('inventory.Inventory', on_delete=models.CASCADE, related_name='inventory_items')
    item = models.ForeignKey('items.Item', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('inventory', 'item')

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"
