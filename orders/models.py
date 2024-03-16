from django.db import models

from users.models import User


class Order(models.Model):
    CREATED = 0
    PAID = 1
    ON_WAY = 3
    DELIVERED = 4

    STATUSES = (
        (CREATED, 'Created'), 
        (PAID, 'Paid'), 
        (ON_WAY, 'On way'), 
        (DELIVERED, 'Delivered'), 
        )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=64)
    owner_surname = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    city = models.CharField(max_length=32)
    adress = models.CharField(max_length=256)
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    order_info = models.JSONField('OrderInfo', default=dict)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(blank=True)

    def __str__(self: object):
        return f'{self.owner_name} {self.owner_surname} - {self.email} - {self.status}'