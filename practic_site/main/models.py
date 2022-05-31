from django.db import models


class Vendor(models.Model):
    name = models.CharField(default='Noname', max_length=150)


class Categoty(models.Model):
    title = models.CharField(default='Untitled', max_length=150)


class Product(models.Model):
    title = models.CharField(default='Untitled', max_length=150)
    rating = models.IntegerField(default=0)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(Categoty, on_delete=models.CASCADE)


