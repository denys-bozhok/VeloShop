from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.FileField(upload_to='images/users', blank=True, null=True)
