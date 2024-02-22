from django.shortcuts import render
from app import utilites

from .filters import all_products


def card_of_product(req: object, slug: str) -> classmethod:
    product = all_products(req).get(slug=slug)
    context = {
        'product': product,
        'title': product.label,
        'colors': product.color.all(),
        'characteristics': product.characteristics.all(),
    }

    context.update(utilites.subheader(req))

    return render(req, 'products/products.html', context)
