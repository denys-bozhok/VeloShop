from django.shortcuts import render
from products.models import *

from . import models, utilites

def home(req):
    transmitted_data = (utilites.get_home_data())
    transmitted_data.update(utilites.get_subheader_data())

    return render(req, 'app/app.html', transmitted_data)


def about(req, about_slug):
    transmitted_data = (utilites.get_about_data(about_slug))
    transmitted_data.update(utilites.get_subheader_data())

    return render(req, 'app/app.html', transmitted_data)


def chapters(req, chapter_slug):
    transmitted_data = (utilites.get_subheader_data())
    transmitted_data.update(utilites.get_categories_data(chapter_slug))

    return render(req, 'app/app.html', transmitted_data)

def category(req, category_slug):
    transmitted_data = utilites.get_subcategories_data(category_slug)
    transmitted_data.update(utilites.get_subheader_data())

    return render(req, 'app/app.html', transmitted_data)


def subcategory(req, category_slug, subcategory_slug):
    subcategory = models.SubCategory.objects.get(slug=subcategory_slug)
    goods = Bicycle.objects.filter(subcategory=subcategory)
    title = subcategory.name

    transmitted_data = {'title': title, 
                        'subcategory': subcategory,
                        'goods': goods}
    
    transmitted_data.update(utilites.get_subheader_data())

    return render(req, 'app/app.html', transmitted_data)
