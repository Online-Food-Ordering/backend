from django.db import models

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField() # price in cents
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
