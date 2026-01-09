# Create your models here.
from django.db import models


class Order(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    items_count = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"
