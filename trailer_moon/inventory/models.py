from django.db import models

class Inventory(models.Model):
    capacity = models.IntegerField(default=20)
    items = models.ManyToManyField('items.Item', through='inventory.InventoryItem')

    def __str__(self):
        return f"Inventory with capacity {self.capacity}"
    

class InventoryItem(models.Model):
    inventory = models.ForeignKey('inventory.Inventory', on_delete=models.CASCADE)
    item = models.ForeignKey('items.Item', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('inventory', 'item')

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"
