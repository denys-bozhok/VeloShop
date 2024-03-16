from django.core.paginator import Paginator
from queryset_sequence import QuerySetSequence

from products.filters import all_products, filters
from carts.models import Cart
from .models import Chapter, SiteNavigation, SocialNetwork, FavoritesAndOther, Language, SubCategory, CharterQuerySet, Category


def pagination(req: object, products, per_page=2) -> classmethod:
    paginator = Paginator(products, per_page)
    page_number = req.GET.get('page')
    page = paginator.get_page(page_number)

    return page


# * -----GET DICTIONARY FOR TEMPLATE-----
def subheader(req: object) -> dict:
    context = {'abouts': CharterQuerySet.all_models(SiteNavigation),
            'social_networks': CharterQuerySet.all_models(SocialNetwork),
            'favorites_and_other': CharterQuerySet.all_models(FavoritesAndOther),
            'languages': CharterQuerySet.all_models(Language)}
    if req.user.is_authenticated:
        cart_items = Cart.objects.filter(user=req.user)
        carts_quantity = 0

        for item in cart_items:
            carts_quantity += item.quantity

        context['carts_quantity'] = carts_quantity
    
    return context


def for_categories(req: object, *args) -> dict:
    context = {}
    try:
        model = Chapter.objects.get(slug=args[0])
        categories = Category.objects.filter(chapter=model)
        products = filters(req, model.name)
        context['categories'] = categories
        context['chapter'] = model
    except:
        try:
            slug = args[1]
            model = SubCategory.objects.get(slug=slug)
            sub_categories = SubCategory.objects.filter(sub_category=model)
            products = filters(req, model.category.chapter.name).filter(subcategory=model)
            context['sub_category'] = model
        except:
            slug = args[0]
            model = Category.objects.get(slug=slug)
            sub_categories = SubCategory.objects.filter(category=model)
            products = filters(req, model.chapter.name).filter(category=model)

        context['category'] = Category.objects.get(slug=args[0])
        context['sub_categories'] = sub_categories

    products_paginator = pagination(req, list(products))
    context['products'] = products_paginator
    context['title'] = model.name

    return context
