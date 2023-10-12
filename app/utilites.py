import products

from . import models


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
    chapter = models.Chapter.objects.get(slug=slug)
    categories = models.Category.objects.filter(chapter=chapter)
    product_list = []

    match(chapter.slug):
        case 'bicycles':
            for category in categories:

                bicycles = products.models.Bicycle.objects.filter(category=category)
                for bicycle in bicycles:
                    product_list.append(bicycle)

        case 'accessories':
            for category in categories:
                accessories = products.models.Accessorie.objects.filter(category=category)

                for accessorie in accessories:
                    product_list.append(accessorie)

        case 'components':
            for category in categories:
                components = products.models.Component.objects.filter(category=category)

                for component in components:
                    product_list.append(component)

        case _:
            return {'msg': 'No products in category'}
        
    title = chapter.name
    chapter_dict = {'categories': categories,
                    'chapter': chapter,
                    'title': title,
                    'product_list': product_list}
    
    return chapter_dict


def get_subcategories_data(slug):
    category = models.Category.objects.get(slug=slug)
    title = category.name
    subcategories = models.SubCategory.objects.filter(category=category)
    product_list = []

    for subcategory in subcategories:
        bicycles = products.models.Bicycle.objects.filter(subcategory=subcategory)
        for bicycle in bicycles:
            product_list.append(bicycle)

        accessories = products.models.Accessorie.objects.filter(subcategory=subcategory)
        for accessorie in accessories:
            product_list.append(accessorie)

        components = products.models.Component.objects.filter(subcategory=subcategory)
        for component in components:
            product_list.append(component)


    chapter_dict = {'subcategories': subcategories,
                    'category': category,
                    'title': title,
                    'product_list': product_list,}

    return chapter_dict
