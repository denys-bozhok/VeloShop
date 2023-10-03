from django.shortcuts import render

from . import models, utilites


def home(req):
    title = 'VeloShop'
    
    transmitted_data = {'title': title}
    transmitted_data.update(utilites.get_subheader_dict())
    transmitted_data.update(utilites.get_chapter_dict())

    return render(req, 'app/app.html', transmitted_data)
    

def chapters(req, chapter_slug):
    title = models.Chapter.objects.get(slug=chapter_slug).name

    transmitted_data = {'title': title}
    transmitted_data.update(utilites.get_subheader_dict())
    transmitted_data.update(utilites.get_category_in_chapter_dict(chapter_slug))

    return render(req, 'app/app.html', transmitted_data)

def category(req, chapter_slug, category_slug):

    title = models.Category.objects.get(slug=category_slug).name

    transmitted_data = {'title': title}
    transmitted_data.update(utilites.get_subheader_dict())
    transmitted_data.update(utilites.get_subcategories_dict(category_slug))

    return render(req, 'app/app.html', transmitted_data)


def subcategory(req, chapter_slug, category_slug, subcategory_slug):
    title = models.SubCategory.objects.get(slug=subcategory_slug).name
    print(title)
    print(chapter_slug)
    print(category_slug)
    print(subcategory_slug)
    transmitted_data = {'title': title}
    return render(req, 'app/app.html', transmitted_data)