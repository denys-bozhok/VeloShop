from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
import os

from app.models import Category, SubCategory


#* -----WRAPPERS-----
#? it`s for rename image of product and create folder by articul 
def products_filename_wrapper(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.article, ext)

    return os.path.join(f'images/products/{instance.article}/', filename)




class ProductsQuerySet(models.QuerySet):
    def get_all_products(self):

        products = []
        bicycles = Bicycle.get_all_bicycles('')
        accessories = Accessorie.objects.all()
        components = Component.objects.all()
        products_list = bicycles, accessories, components

        i = 0

        while i < len(products_list):
            for product in products_list[i]:
                products.append(product)
                i += 1

        return products


# * -----PRODUCT`S INCLUDES-----
class Manufacturer(models.Model):
    name = models.CharField(max_length=20, unique=True)
    image = models.FileField(upload_to='images/manufactirers/')
    description = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=30, editable=False, auto_created=True)

    def save(self):
        self.slug = slugify(self.name)
        super().save()

    def __str__(self):
        return f'{self.name}'


class Color(models.Model):
    color = models.CharField(max_length=10)
    rgb = models.CharField(max_length=13)

    def __str__(self):
        return f'{self.color}'


class Size(models.Model):
    short_name = models.CharField(max_length=5)
    minimal = models.IntegerField(validators=[MinValueValidator(0)])
    maximal = models.IntegerField(validators=[MinValueValidator(0)])
    
    def __str__(self):
        return f'{self.short_name} ({self.minimal} - {self.minimal}cm)'


class WheelSize(models.Model):
    size = models.DecimalField(max_digits=10, decimal_places=1, unique=True, validators=[MinValueValidator(6),])

    def __str__(self):
        return f'{self.size}'


class SuspensionTravel(models.Model):
    suspension_travel = models.FloatField(validators=[MinValueValidator(0),],)

    def __str__(self):

        return f'{self.suspension_travel}mm'


class Material(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.name}'
    

class Weight(models.Model):
    weight = models.FloatField(validators=[MinValueValidator(0),])
    
    def __str__(self):
        return f'{self.weight}kg'


class Characteristic(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return f'{self.name}'
    

class CharacteristicValue(models.Model):
    name = models.ForeignKey(Characteristic, on_delete=models.CASCADE)
    description = models.TextField(max_length=50)

    def __str__(self):
        return f'{self.name} - {self.description}'


# * -----PRODUCTS-----
class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, blank=True,null=True, on_delete=models.DO_NOTHING)
    label = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    article = models.CharField(max_length=30, unique=True)
    characteristics = models.ManyToManyField(CharacteristicValue, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING, blank=True, null=True)
    rating = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    value = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    slug = models.CharField(max_length=30, editable=False, auto_created=True)
    image = models.FileField(upload_to=products_filename_wrapper, blank=True)
    
    def save(self):
        self.slug = slugify(self.label)
        super().save()

    def __str__(self):
        return f'{self.label}/{self.category}'
    
    class Meta:
        abstract = True


class Bicycle(Product):
    model = models.CharField(max_length=20)
    color = models.ManyToManyField(Color)
    wheel = models.ForeignKey(WheelSize, on_delete=models.DO_NOTHING)
    frame_size = models.ForeignKey(Size, on_delete=models.DO_NOTHING)
    frame_material = models.ForeignKey(Material, on_delete=models.DO_NOTHING)
    suspension = models.BooleanField(default=False)
    suspension_travel = models.ForeignKey(SuspensionTravel, on_delete=models.DO_NOTHING, blank=True, null=True)
    weight = models.ForeignKey(Weight, on_delete=models.DO_NOTHING, blank=True, null=True)
    year = models.IntegerField(validators=[MinValueValidator(2000)], blank=True, null=True)



class BicycleGalery(models.Model):
    product = models.ForeignKey(Bicycle, default=None, on_delete=models.CASCADE)
    article = models.CharField(max_length=30, editable=False, auto_created=True)
    image = models.FileField(upload_to=products_filename_wrapper, blank=True)
 
    def __str__(self):
        return self.product.article
    
    def save(self):
        self.article = self.product.article
        super().save()
    

class Accessorie(Product):
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.DO_NOTHING, blank=True, null=True)
    weight = models.ForeignKey(Weight, on_delete=models.DO_NOTHING, blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)


class AccessorieGalery(models.Model):
    product = models.ForeignKey(Accessorie, default=None, on_delete=models.CASCADE)
    article = models.CharField(max_length=30,editable=False, auto_created=True)
    image = models.FileField(upload_to=products_filename_wrapper, blank=True)

    def __str__(self):
        return self.product.article
    
    def save(self):
        self.article = self.product.article
        super().save()


class Component(Product):
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.DO_NOTHING, blank=True, null=True)
    weight = models.ForeignKey(Weight, on_delete=models.DO_NOTHING, blank=True, null=True)
    model = models.CharField(max_length=20, blank=True, null=True)


class ComponentGalery(models.Model):
    product = models.ForeignKey(Component, default=None, on_delete=models.CASCADE)
    article = models.CharField(max_length=30,editable=False, auto_created=True)
    image = models.FileField(upload_to=products_filename_wrapper, blank=True)

    def __str__(self):
        return self.product.article
    
    def save(self):
        self.article = self.product.article
        super().save()