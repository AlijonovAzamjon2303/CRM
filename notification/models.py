from django.db import models
from store.models import Store

class Notification(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification: {self.message[:30]}..."
