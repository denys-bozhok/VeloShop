from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app import utilites
from . import models


def card_of_product(req, slug):
    products = models.ProductsQuerySet.all_products('')

    for item in products:
        if item.slug == slug:
            product = item


    context = {
        'product': product,
        'galery': models.ProductsQuerySet.gallery_for_product('', product),
        'title': product.label,
        'colors': product.color.all(),
        'characteristics': product.characteristics.all(),
    }

    context.update(utilites.subheader())

    return render(req, 'products/products.html', context)
