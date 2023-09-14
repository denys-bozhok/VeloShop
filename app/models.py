from django.db import models


class Chapter(models.Model):
    pass


class Category(models.Model):
    pass


class Product(models.Model):
    
    class Meta:
        abstract = True


class Bicycle(models.Model):
    pass


class Helmet(models.Model):
    pass


class Lighting(models.Model):
    pass