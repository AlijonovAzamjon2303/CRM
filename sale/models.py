from django.db import models
from store.models import Store
from product.models import Product
from inventory.models import Inventory
from django.core.exceptions import ValidationError

class Sale(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='sales')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    sold_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Mahsulot narxi asosida total price hisoblash
        self.total_price = self.quantity * self.product.price

        # Inventory ni topamiz
        try:
            inventory = Inventory.objects.get(store=self.store, product=self.product)
        except Inventory.DoesNotExist:
            raise ValidationError(f"{self.store.name} do‘konida {self.product.name} mahsuloti mavjud emas.")

        # Yetarli mahsulot borligini tekshiramiz
        if inventory.quantity < self.quantity:
            raise ValidationError(f"Yetarli zaxira yo‘q: mavjud {inventory.quantity} dona.")

        # Zaxiradan ayiramiz
        inventory.quantity -= self.quantity
        inventory.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} @ {self.store.name}"
