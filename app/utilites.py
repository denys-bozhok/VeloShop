from django.core.paginator import Paginator
from queryset_sequence import QuerySetSequence

from products.filters import all_products
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
            'languages': CharterQuerySet.all_models(Language)}


def for_categories(req: object, *args) -> dict:
    context = {}
    try:
        model = Chapter.objects.get(slug=args[0])
        products = []
        categories = Category.objects.filter(chapter=model)

        for category in categories:
            products += all_products().filter(category=category)

        products = QuerySetSequence(products)

        context['categories'] = categories
        context['chapter'] = model

    except:
        try:
            slug = args[1]
            model = SubCategory.objects.get(slug=slug)
            sub_categories = SubCategory.objects.filter(sub_category=model)
            products = all_products().filter(subcategory=model)

            context['sub_category'] = model
        except:
            slug = args[0]
            model = Category.objects.get(slug=slug)
            sub_categories = SubCategory.objects.filter(category=model)
            products = all_products().filter(category=model)

        context['category'] = Category.objects.get(slug=args[0])
        context['sub_categories'] = sub_categories

    products_paginator = pagination(req, list(products))
    context['products'] = products_paginator
    context['title'] = model.name

    return context
