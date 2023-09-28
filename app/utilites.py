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
