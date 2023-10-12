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
    title = subcategory.name
    product_list = []

    bicycles = Bicycle.objects.filter(subcategory=subcategory)

    for bicycle in bicycles:
        product_list.append(bicycle)

    if product_list == []:
        components = Component.objects.filter(subcategory=subcategory)
        for component in components:
            product_list.append(component)

    if product_list == []:
        accessories = Accessorie.objects.filter(subcategory=subcategory)
        for accessorie in accessories:
            product_list.append(accessorie)

    transmitted_data = {'title': title, 
                        'subcategory': subcategory,
                        'product_list': product_list,}
    
    transmitted_data.update(utilites.get_subheader_data())

    return render(req, 'app/app.html', transmitted_data)