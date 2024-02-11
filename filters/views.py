from django.shortcuts import render

from . import models


def filtred_list(req, products):
    filterset = models.ProductFilter.filter_products(req, products)

    return {'filters': filterset}
