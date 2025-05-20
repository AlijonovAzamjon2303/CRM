from django.db import models
from store.models import Store
from product.models import Product

class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='inventories')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventories')
    quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} @ {self.store.name}: {self.quantity} dona"

    class Meta:
        unique_together = ('store', 'product')
