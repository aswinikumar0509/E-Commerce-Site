from django.db import models

# Create your models here.

class Product(models.Model):

    title = models.CharField(max_length=500)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=500)
    description = models.TextField()
    image = models.CharField(max_length=1000)
