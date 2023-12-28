from django.core.paginator import Paginator

from products.models import ProductsQuerySet
from carts.utilites import for_cart_detail
from .models import SiteNavigation, SocialNetwork, FavoritesAndOther, Language, SubCategory, CharterQuerySet, Category
from carts.utilites import for_cart_detail


# * -----GET DICTIONARY FOR TEMPLATE-----
def pagination(req, products, per_page):

    paginator = Paginator(products, per_page)
    page_number = req.GET.get('page')
    page = paginator.get_page(page_number)

    return page


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

            products_paginator = pagination(req, products, 2)

            return {'categories': categories,
                    'chapter': chapter,
                    'title': chapter.name,
                    'products': products_paginator}

        case 'Category':
            category = model.objects.get(slug=slug)
            sub_categories = SubCategory.objects.filter(category=category)

            products = list(filter(lambda product: product.category.slug ==
                            slug, ProductsQuerySet.all_products('')))

            products_paginator = pagination(req, products, 2)

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

            products_paginator = pagination(req, products, 2)

            return {'sub_categories': sub_categories,
                    'sub_category': sub_category,
                    'title': sub_category.name,
                    'products': products_paginator,
                    'category': category}

        case _:
            return
