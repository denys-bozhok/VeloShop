from django.core.paginator import Paginator

from products.models import ProductsQuerySet
from carts.utilites import for_cart_detail
from .models import SiteNavigation, SocialNetwork, FavoritesAndOther, Language, SubCategory, CharterQuerySet, Category
from carts.utilites import for_cart_detail


# * -----FILTERES-----
def filterset(req: object, products: list) -> list:
    wheel = req.GET.get('wheel')
    rating = req.GET.get('rating')
    filtred_products = []

    for product in products:
        if product.rating.__str__() == rating:
            filtred_products.append(product)

        if product.wheel.__str__() == wheel:
            filtred_products.append(product)

    for filtred_product in filtred_products:
        if rating:
            if filtred_product.rating.__str__() != rating:
                filtred_products.remove(filtred_product)

        if wheel:
            if filtred_product.wheel.__str__() != wheel:
                filtred_products.remove(filtred_product)

    filtred_products = list(set(filtred_products))

    if filtred_products != []:
        products = filtred_products

    return products


def pagination(req: object, products: list, per_page=2) -> classmethod:
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


def for_categories(req, slug: str, model: object, *category_slug: str) -> dict:
    match(model.__name__):
        case 'Chapter':
            chapter = model.objects.get(slug=slug)
            categories = Category.objects.filter(chapter=chapter)

            products = list(filter(lambda product: product.category.chapter.slug ==
                            slug, ProductsQuerySet.all_products('')))

            products = filterset(req, products)

            products_paginator = pagination(req, products)

            return {'categories': categories,
                    'chapter': chapter,
                    'title': chapter.name,
                    'products': products_paginator}

        case 'Category':
            category = model.objects.get(slug=slug)
            sub_categories = SubCategory.objects.filter(category=category)

            products = list(filter(lambda product: product.category.slug ==
                            slug, ProductsQuerySet.all_products('')))

            products = filterset(req, products)

            products_paginator = pagination(req, products)

            return {'sub_categories': sub_categories,
                    'category': category,
                    'title': category.name,
                    'products': products_paginator}

        case 'SubCategory':
            sub_category = model.objects.get(slug=slug)
            sub_categories = SubCategory.objects.filter(
                sub_category=sub_category)
            category_slug = category_slug[0]
            category = Category.objects.get(slug=category_slug)

            products = list(filter(lambda product: product.subcategory.slug ==
                            slug, ProductsQuerySet.all_products('')))

            products = filterset(req, products)

            products_paginator = pagination(req, products)

            return {'sub_categories': sub_categories,
                    'sub_category': sub_category,
                    'title': sub_category.name,
                    'products': products_paginator,
                    'category': category}

        case _:
            return
