import products

from . import models



def get_product_in_category(categories):
    goods = []

    for category in categories:
        try:
            goods.append(products.models.Bicycle.objects.get(category=category))
        except:
            pass
        
        try:
            goods.append(products.models.Bicycle.objects.get(subcategory=category))
        except:
            pass
        
        try:
            goods.append(products.models.Hamlet.objects.get(category=category))
        except:
            pass

    return goods


#* -----GET DICTIONARY FOR TEMPLATE-----

def get_subheader_data():
    site_navigations = models.SiteNavigation.objects.all()
    social_networks = models.SocialNetwork.objects.all()
    favorites_and_other = models.FavoritesAndOther.objects.all()
    languages = models.Language.objects.all()

    subheader_dict = {
        'site_navigations': site_navigations,
        'social_networks': social_networks,
        'favorites_and_other': favorites_and_other,
        'languages': languages,
    }

    return subheader_dict


def get_about_data(slug):
    site_navigate = models.SiteNavigation.objects.get(slug=slug)
    title = site_navigate.name
    site_navigate_dict = {'title': title, 'site_navigate': site_navigate}
    
    return site_navigate_dict


def get_home_data():
    title = 'VeloShop'
    chapters = models.Chapter.objects.all()
    chapters_dict = {'title': title, 'chapters': chapters}

    return chapters_dict


def get_categories_data(slug):
    try:
        chapter = models.Chapter.objects.get(slug=slug)
        categories = models.Category.objects.filter(chapter_id=chapter.id)
        goods = get_product_in_category(categories)
        title = chapter.name
        chapter_dict = {'categories': categories,
                        'chapter': chapter,
                        'title': title,
                        'goods': goods}

    except:
        chapter_dict = {}

    
    return chapter_dict


def get_subcategories_data(slug):
    category = models.Category.objects.get(slug=slug)
    title = category.name
    subcategories = models.SubCategory.objects.filter(category_id=category.id)

    goods = get_product_in_category(subcategories)

    chapter_dict = {'subcategories': subcategories,
                    'category': category,
                    'title': title,
                    'goods': goods,}

    return chapter_dict
