from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify

import os


#* -----WRAPPERS-----

#? it`s for rename image of product and create folder by articul 
def products_filename_wrapper(instance, filename):
    
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.article, ext)
    
    # if Product.objects.get(image=f"images/products/{filename}"):
    #     Product.objects.get(image=f"images/products/{filename}").image.delete(save=True)
    
    return os.path.join(f'images/products/{instance.article}/', filename)


# * -----CATEGORIES-----
class Chapter(models.Model):
    name = models.CharField(max_length=20, 
                            unique=True)
    image = models.FileField(upload_to='images/categories/')
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
    image = models.FileField(upload_to='images/categories/')
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
class Manufacturer(models.Model):
    name = models.CharField(max_length=20, unique=True)
    image = models.FileField(upload_to='images/categories/')
    description = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=30, 
                            editable=False, 
                            auto_created=True)

    def save(self):
        self.slug = slugify(self.name)
        super().save()

    def __str__(self):
        return f'{self.name}'


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
    image = models.FileField(upload_to='images/sizes/')
    
    def __str__(self):
        return f'{self.size}'


class WheelSize(models.Model):
    size = models.DecimalField(max_digits=3, 
                               decimal_places=1,
                               unique=True,
                               validators=[MinValueValidator(6), 
                                           MaxValueValidator(31)],)
    image = models.FileField(upload_to='images/sizes/')

    def __str__(self):
        return f'{self.size}'


class Characteristic(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    
    def __str__(self):
        return f'{self.name}'


# * -----PRODUCTS-----
class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer,
                                     blank=True,
                                     null=True, 
                                     on_delete=models.DO_NOTHING)
    label = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    article = models.CharField(max_length=30, unique=True)
    image = models.FileField(upload_to=products_filename_wrapper)
    characteristics = models.ManyToManyField(Characteristic, blank=True)
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
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING)
    wheel = models.ForeignKey(WheelSize, on_delete=models.DO_NOTHING)
    frame = models.ForeignKey(FrameSize, on_delete=models.DO_NOTHING)
    year = models.IntegerField(validators=[MinValueValidator(2000)], 
                               blank=True, 
                               null=True)
    

class Helmet(Product):
    pass


class Lighting(Product):
    pass