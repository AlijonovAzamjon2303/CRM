from django.db import models
from store.models import Store

class Product(models.Model):
    name = models.CharField(max_length=100)
    barcode = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
