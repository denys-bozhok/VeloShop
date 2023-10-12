from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify

from app.models import Category, Chapter, SubCategory
import os


#* -----WRAPPERS-----
#? it`s for rename image of product and create folder by articul 
def products_filename_wrapper(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.article, ext)
#? for delete image, if filename is reserved
    # if Product.objects.get(image=f"images/products/{filename}"):
    #     Product.objects.get(image=f"images/products/{filename}").image.delete(save=True)
    return os.path.join(f'images/products/{instance.article}/', filename)



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
    first_color = models.CharField(max_length=10)
    second_color = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f'{self.first_color}, {self.second_color}'


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
        return f'{self.weight}g'


class CharacteristicTitle(models.Model):
    name = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return f'{self.name}'
    

class CharacteristicDescription(models.Model):
    name = models.ForeignKey(CharacteristicTitle, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.description}'


# * -----PRODUCTS-----
class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, blank=True,null=True, on_delete=models.DO_NOTHING)
    label = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    article = models.CharField(max_length=30, unique=True)
    characteristics = models.ForeignKey(CharacteristicDescription, on_delete=models.CASCADE, blank=True)
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
        return f'{self.label}'

    class Meta:
        abstract = True


class Bicycle(Product):
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING)
    wheel = models.ForeignKey(WheelSize, on_delete=models.DO_NOTHING)
    frame_size = models.ForeignKey(Size, on_delete=models.DO_NOTHING)
    frame_material = models.ForeignKey(Material, on_delete=models.DO_NOTHING)
    suspension = models.BooleanField(default=False)
    suspension_travel = models.ForeignKey(SuspensionTravel, on_delete=models.DO_NOTHING)
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
    

class Hamlet(Product):
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING)
    size = models.ForeignKey(Size, on_delete=models.DO_NOTHING)
    weight = models.ForeignKey(Weight, on_delete=models.DO_NOTHING, blank=True, null=True)


class HamletGalery(models.Model):
    product = models.ForeignKey(Hamlet, default=None, on_delete=models.CASCADE)
    article = models.CharField(max_length=30,editable=False, auto_created=True)
    image = models.FileField(upload_to=products_filename_wrapper, blank=True)

    def __str__(self):
        return self.product.article
    
    def save(self):
        self.article = self.product.article
        super().save()


class Lighting(Product):
    pass

