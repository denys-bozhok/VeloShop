from products.models import ProductsQuerySet

from .models import SiteNavigation, SocialNetwork, FavoritesAndOther, Language, SubCategory, CharterQuerySet, Category, Chapter


#* -----GET DICTIONARY FOR TEMPLATE-----

def subheader() -> dict:
    context = {'abouts': CharterQuerySet.all_models(SiteNavigation),
               'social_networks': CharterQuerySet.all_models(SocialNetwork),
               'favorites_and_other': CharterQuerySet.all_models(FavoritesAndOther),
               'languages': CharterQuerySet.all_models(Language)}

    return context


def for_categories(slug:str, model:object, *category_slug:str) -> dict:
    match(model.__name__):
        case 'Chapter':
            chapter = Chapter.objects.get(slug=slug)
            categories = Category.objects.filter(chapter=chapter)
            products = list(filter(lambda product: product.category.chapter.slug == slug, ProductsQuerySet.all_products('')))

            return {'categories': categories,'chapter': chapter,'title': chapter.name,'products': products}
        
        case 'Category':
            category = Category.objects.get(slug=slug)
            sub_categories = SubCategory.objects.filter(category=category)
            products = list(filter(lambda product: product.category.slug == slug, ProductsQuerySet.all_products('')))

            return {'sub_categories': sub_categories,'category': category, 'title': category.name, 'products': products}
        
        case 'SubCategory':
            sub_category = SubCategory.objects.get(slug=slug)
            sub_categories = SubCategory.objects.filter(sub_category=sub_category)
            category_slug = category_slug[0]
            category = Category.objects.get(slug=category_slug)
            products = list(filter(lambda product: product.subcategory.slug == slug, ProductsQuerySet.all_products('')))

            return {'sub_categories': sub_categories,'sub_category': sub_category, 
                    'title': sub_category.name, 'products': products, 'category': category}
                
        case _:
            return