from django.db import models

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify

from . import utilites


# * -----TEMPLATE`S ELEMENTS-----
class SiteNavigation (models.Model):
    name = models.CharField(max_length=20, 
                            unique=True)
    
    description = models.TextField()
    
    slug = models.CharField(max_length=30, 
                            editable=False, 
                            auto_created=True)
    def save(self):
        self.slug = slugify(self.name)
        super().save()
    
    def __str__(self):
        return f'{self.name}'
    
    
class SocialNetwork (models.Model):
    name = models.CharField(max_length=20, 
                            unique=True)
    
    image = models.FileField(upload_to='images/icons/social_networks')
    link = models.CharField(max_length=50, default='#', unique=True)
    
    def __str__(self):
        return f'{self.name}'


class FavoritesAndOther (models.Model):
    name = models.CharField(max_length=20, 
                            unique=True)
    
    icon = models.FileField(upload_to='images/icons/favorites_and_other')
    
    value = models.IntegerField(default=0, 
                                validators=[MinValueValidator(0)])
    
    slug = models.CharField(max_length=30, 
                            editable=False, 
                            auto_created=True)
    def save(self):
        self.slug = slugify(self.name)
        super().save()
    
    def __str__(self):
        return f'{self.name}'


class Language(models.Model):
    name = models.CharField(max_length=20, 
                            unique=True)
    
    icon = models.FileField(upload_to='images/icons/languages')
    
    short_name = models.CharField(max_length=3, 
                            unique=True)
    
    slug = models.CharField(max_length=30, 
                            editable=False, 
                            auto_created=True)

    def save(self):
        self.slug = slugify(self.short_name)
        super().save()

    def __str__(self):
        return f'{self.name} ({self.short_name})'
    

# * -----CATEGORIES-----
class Chapter(models.Model):
    name = models.CharField(max_length=20, 
                            unique=True)
    
    image = models.FileField(upload_to='images/icons/categories/')
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
    image = models.FileField(upload_to='images/icons/categories/')
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
    

class SubCategory(models.Model):
    name = models.CharField(max_length=20, unique=True)
    image = models.FileField(upload_to='images/icons/categories/')
    description = models.TextField(blank=True, null=True)
    
    category = models.ForeignKey(Category, 
                                 blank=True,
                                 null=True, 
                                 on_delete=models.DO_NOTHING)
    
    sub_category = models.ForeignKey('self',
                                     blank=True,
                                     null=True, 
                                     on_delete=models.DO_NOTHING)

    slug = models.CharField(max_length=30, 
                            editable=False, 
                            auto_created=True)

    def save(self):
        self.slug = slugify(self.name)
        super().save()

    def __str__(self):
        return f'{self.name}'