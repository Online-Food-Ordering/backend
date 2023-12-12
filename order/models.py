from django.db import models

from food.models import Food


# Create your models here.


class Order(models.Model):
    order_status = models.CharField(max_length=100)
    total = models.IntegerField()  # price in cents
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
