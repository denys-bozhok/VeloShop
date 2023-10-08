from django.shortcuts import render
from products.models import *
from . import models, utilites

def home(req):
    transmitted_data = (utilites.get_chapter_dict())
    transmitted_data.update(utilites.get_subheader_dict())

    return render(req, 'app/app.html', transmitted_data)


def about(req, about_slug):
    transmitted_data = (utilites.get_site_navigate(about_slug))
    transmitted_data.update(utilites.get_subheader_dict())

    return render(req, 'app/app.html', transmitted_data)


def chapters(req, chapter_slug):
    transmitted_data = (utilites.get_category_in_chapter_dict(chapter_slug))
    transmitted_data.update(utilites.get_subheader_dict())

    return render(req, 'app/app.html', transmitted_data)

def category(req, category_slug):
    transmitted_data = (utilites.get_subcategories_dict(category_slug))
    transmitted_data.update(utilites.get_subheader_dict())

    return render(req, 'app/app.html', transmitted_data)


def subcategory(req, category_slug, subcategory_slug):
    subcategory = models.SubCategory.objects.get(slug=subcategory_slug)
    subcategories = models.SubCategory.objects.filter(sub_category=subcategory.id)
    title = subcategory.name

    transmitted_data = {'title': title, 
                        'subcategories': subcategories, 
                        'subcategory': subcategory}
    
    transmitted_data.update(utilites.get_subheader_dict())

    return render(req, 'app/app.html', transmitted_data)