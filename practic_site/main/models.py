from django.db import models


class Vendor(models.Model):
    name = models.CharField(default='Noname', max_length=150)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(default='Untitled', max_length=150)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(default='Untitled', max_length=150)
    buy_rating = models.IntegerField(default=0)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def buy(self):
        self.buy_rating += 1


