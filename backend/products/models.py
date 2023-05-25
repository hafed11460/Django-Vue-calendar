from django.db import models

# Create your models here.

class Product (models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class PackageFeature(models.Model):
    title = models.CharField(max_length=100)


class Package(models.Model):
    name = models.CharField(max_length=100, unique=True)
    monthly_price = models.DecimalField(default=10, decimal_places=2, max_digits=6)
    annual_price = models.DecimalField(default=10, decimal_places=2, max_digits=6)
    features  = models.ManyToManyField("PackageFeature")

    def __str__(self):
        return self.name
