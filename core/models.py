from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    title = models.CharField(max_length=255, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=50, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
