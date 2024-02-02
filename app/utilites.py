from django.core.paginator import Paginator

from filters.views import filtred_list
from filters.models import ProductFilter
from carts.utilites import for_cart_detail
from carts.utilites import for_cart_detail
from .models import Chapter, SiteNavigation, SocialNetwork, FavoritesAndOther, Language, SubCategory, CharterQuerySet, Category


def pagination(req: object, products, per_page=2) -> classmethod:
    paginator = Paginator(products, per_page)
    page_number = req.GET.get('page')
    page = paginator.get_page(page_number)

    return page


# * -----GET DICTIONARY FOR TEMPLATE-----
def subheader(req: object) -> dict:
    return {'abouts': CharterQuerySet.all_models(SiteNavigation),
            'social_networks': CharterQuerySet.all_models(SocialNetwork),
            'favorites_and_other': CharterQuerySet.all_models(FavoritesAndOther),
            'languages': CharterQuerySet.all_models(Language),
            'cart_lenth': for_cart_detail(req)['items_quantity']}


def for_categories(req: object, *args) -> dict:
    context = {}
    products = []

    try:
        model = Chapter.objects.get(slug=args[0])
        categories = Category.objects.filter(chapter=model)

        for category in categories:
            products += ProductFilter.product_filter_by_category(category)

        filtred_products = ProductFilter.filter_products(req, products)
        products = filtred_products

        context['categories'] = Category.objects.filter(chapter=model)
        context['chapter'] = model

    except:
        try:
            model = SubCategory.objects.get(slug=args[1])
            sub_categories = SubCategory.objects.filter(sub_category=model)
            context['sub_category'] = model
        except:
            model = Category.objects.get(slug=args[0])
            sub_categories = SubCategory.objects.filter(category=model)

        products += ProductFilter.product_filter_by_category(model)

        filtred_products = ProductFilter.filter_products(req, products)
        products = filtred_products

        context['category'] = Category.objects.get(slug=args[0])
        context['sub_categories'] = sub_categories

    products_paginator = pagination(req, list(products))
    context['products'] = products_paginator
    context['title'] = model.name

    return context
