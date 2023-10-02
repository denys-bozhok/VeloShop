from . import models


#* -----GET DICTIONARY FOR TEMPLATE-----
def get_subheader_dict():
    
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

def get_chapter_dict():
    chapters = models.Chapter.objects.all()
    
    chapter_dict = {'chapters': chapters}

    return chapter_dict


def get_category_in_chapter_dict(slug):
    chapter = models.Chapter.objects.get(slug=slug)
    categories = models.Category.objects.filter(chapter=chapter)
    chapter_dict = {'categories': categories,
                    'chapter': chapter}

    return chapter_dict

def get_subcategories_dict(slug):
    category = models.Category.objects.get(slug=slug)
    subcategories = models.SubCategory.objects.filter(category=category)
    chapter_dict = {'subcategories': subcategories,
                    'category': category}

    return chapter_dict
