from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)