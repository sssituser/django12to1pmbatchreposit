from django.db import models

# Create your models here.
class Product(models.Model):
    prodid = models.IntegerField()
    prodname = models.CharField(max_length=30)
    proprice = models.IntegerField()
    proqty = models.IntegerField()