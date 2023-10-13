from django.db import models
from users.models import User
from products.models import Bicycle, Accessorie, Component


class BasketQuarySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)
    
    def total_quantity(self):
        return sum(basket.quantity() for basket in self)


class Basket (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bicycles = models.ManyToManyField(Bicycle)
    acsessories = models.ManyToManyField(Accessorie)
    components = models.ManyToManyField(Component)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuarySet.as_manager()

    def __str__(self):
        return f'Basket for {self.user.username}'

    # def sum(self):
    #     return self.product.price * self.bicycles[]