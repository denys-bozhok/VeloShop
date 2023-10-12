from django.shortcuts import render

from app import utilites
from . import models


# Create your views here.

def card_of_product(req, slug):
    if models.Bicycle.objects.get(slug=slug):
        product = models.Bicycle.objects.get(slug=slug)
        galery = models.BicycleGalery.objects.filter(article=product.article)

    elif models.Accessorie.objects.get(slug=slug):
        product = models.Accessorie.objects.get(slug=slug)
        galery = models.AccessorieGalery.objects.filter(article=product.article)

    else:
        product = models.Component.objects.get(slug=slug)
        galery = models.ComponentGalery.objects.filter(article=product.article)

    title = product.label
    colors = models.Bicycle.objects.get(id=product.id).color.all()
    characteristics = models.Bicycle.objects.get(id=product.id).characteristics.all()
    
    print(characteristics)

    transmision_data = {
        'product': product,
        'title': title,
        'galery': galery,
        'colors': colors,
        'characteristics': characteristics,
    }

    transmision_data.update(utilites.get_subheader_data())

    return render(req, 'products/products.html', transmision_data)


