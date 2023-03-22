from django.db import models


# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=250)
    description=models.CharField(max_length=1000)
    price=models.DecimalField(max_digits=20, decimal_places=2)
    inventory_quantity=models.IntegerField(default=0)
    picture = models.CharField(blank=True, null=True,max_length=250)