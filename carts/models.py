from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse

from users.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.JSONField(default=dict)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product["label"]}"

    def get_absolute_url(self):
        return reverse("carts:cart_detail")

    def product_sum(self):
        return self.product['price'] * self.quantity
