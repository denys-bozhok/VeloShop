from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify

import os


# * -----WRAPPERS-----
def products_filename_wrapper(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.article, ext)

    return os.path.join(f'products/{instance.article}/', filename)


def size_filename_wrapper(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.size, ext)
    
    return os.path.join(f'sizes/{instance.size}/', filename)


def category_filename_wrapper(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.name, ext)
    
    return os.path.join(f'category/{instance.name}/', filename)


# * -----CATEGORIES-----
class Chapter(models.Model):
    name = models.CharField(max_length=20, 
                            unique=True)
    image = models.FileField(upload_to=category_filename_wrapper)
    description = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=30, 
                            editable=False, 
                            auto_created=True)

    def save(self):
        self.slug = slugify(self.name)
        super().save()

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    image = models.FileField(upload_to=category_filename_wrapper)
    description = models.TextField(blank=True, null=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    slug = models.CharField(max_length=30, 
                            editable=False, 
                            auto_created=True)

    def save(self):
        self.slug = slugify(self.name)
        super().save()

    def __str__(self):
        return f'{self.name}'


# * -----INCLUDES-----
class Color(models.Model):
    name = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return f'{self.name}'


class FrameSize(models.Model):
    size = models.DecimalField(max_digits=3, 
                               decimal_places=1,
                               unique=True,
                               validators=[MinValueValidator(6), 
                                           MaxValueValidator(31)],)
    image = models.FileField(upload_to=size_filename_wrapper)
    
    def __str__(self):
        return f'{self.size}'


class WheelSize(models.Model):
    size = models.DecimalField(max_digits=3, 
                               decimal_places=1,
                               unique=True,
                               validators=[MinValueValidator(6), 
                                           MaxValueValidator(31)],)
    image = models.FileField(upload_to=size_filename_wrapper)

    def __str__(self):
        return f'{self.size}'


class Characteristics(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()


# * -----PRODUCTS-----
class Product(models.Model):
    label = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    article = models.CharField(max_length=30, unique=True)
    image = models.FileField(upload_to=products_filename_wrapper)
    characteristics = models.ManyToManyField(Characteristics, blank=True)
    category = models.ForeignKey(Category, 
                                 on_delete=models.DO_NOTHING, 
                                 blank=True, 
                                 null=True)
    
    rating = models.FloatField(default=0,
                               validators=[MinValueValidator(0), 
                                           MaxValueValidator(5)])
    
    value = models.IntegerField(default=0, 
                                validators=[MinValueValidator(0)])
    
    slug = models.CharField(max_length=30, 
                            editable=False, 
                            auto_created=True)
    
    def save(self):
        self.slug = slugify(self.label)
        super().save()

    def __str__(self):
        return f'{self.label}'

    class Meta:
        abstract = True


class Bicycle(Product):
    pass


class Helmet(Product):
    pass


class Lighting(Product):
    pass