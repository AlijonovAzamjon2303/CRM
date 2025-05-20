from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_stores')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
