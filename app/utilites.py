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


def get_site_navigate(slug):
    site_navigate = models.SiteNavigation.objects.get(slug=slug)
    title = site_navigate.name
    site_navigate_dict = {'title': title, 'site_navigate': site_navigate}

    return site_navigate_dict

def get_chapter_dict():
    title = 'VeloShop'
    chapters = models.Chapter.objects.all()
    chapters_dict = {'title': title, 'chapters': chapters}

    return chapters_dict


def get_category_in_chapter_dict(slug):
    chapter = models.Chapter.objects.get(slug=slug)
    title = chapter.name
    categories = models.Category.objects.filter(chapter=chapter)
    chapter_dict = {'categories': categories,
                    'chapter': chapter,
                    'title': title}

    return chapter_dict

def get_subcategories_dict(slug):
    category = models.Category.objects.get(slug=slug)
    title = category.name
    subcategories = models.SubCategory.objects.filter(category=category).filter(sub_category=None)
    chapter_dict = {'subcategories': subcategories,
                    'category': category,
                    'title': title}

    return chapter_dict
