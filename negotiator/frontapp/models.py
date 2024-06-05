from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    category =models.CharField(max_length=100)
    listed_price = models.DecimalField(max_digits=10, decimal_places=2)
    min_profitable_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=100)

    