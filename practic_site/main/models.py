from django.db import models


class Pizza(models.Model):
    title = models.CharField(default='Untitled', max_length=50)
    cost = models.IntegerField(default=400)

    def __str__(self):
        return self.title


class Buyer(models.Model):
    email = models.EmailField(max_length=80)
    name = models.CharField(max_length=100)
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.email


class Order(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    

class OrderElement(models.Model):
    pizza_id = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)


