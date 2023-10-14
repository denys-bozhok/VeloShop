from products.models import ProductsQuerySet

from .models import SiteNavigation, SocialNetwork, FavoritesAndOther, Language, SubCategory, CharterQuerySet, Category, Chapter


#* -----GET DICTIONARY FOR TEMPLATE-----

def subheader() -> dict:
    context = {
        'abouts': CharterQuerySet.all_models(SiteNavigation),
        'social_networks': CharterQuerySet.all_models(SocialNetwork),
        'favorites_and_other': CharterQuerySet.all_models(FavoritesAndOther),
        'languages': CharterQuerySet.all_models(Language)
        }

    return context


def for_categories(slug:str, model:object) -> dict:
    match(model.__name__):
        case 'Chapter':
            print(model.__name__)
            chapter = CharterQuerySet.model_by_slug(Chapter, slug)
            categories = Category.objects.filter(chapter=chapter)
            products = list(filter(lambda product: product.category.chapter.slug == slug, ProductsQuerySet.all_products('')))
            return {'categories': categories,'chapter': chapter,'title': chapter.name,'products': products}
        
        case 'Category':
            print(model.__name__)
            category = CharterQuerySet.model_by_slug(model, slug)
            subcategories = SubCategory.objects.filter(slug=slug)
            products = list(filter(lambda product: product.category.slug == slug, ProductsQuerySet.all_products('')))
            return {'subcategories': subcategories,'category': category, 'title': category.name, 'products': products}
        
        case 'SubCategory':
            print(model.__name__)
            subcategory = CharterQuerySet.model_by_slug(model, slug)
            subcategories = SubCategory.objects.filter(slug=slug)
            products = list(filter(lambda product: product.subcategory.slug == slug, ProductsQuerySet.all_products('')))
            return {'subcategories': subcategories,'subcategory': subcategory, 'title': subcategory.name, 'products': products}
                
        case _:
            return