from django.contrib import admin

from .models import *


admin.site.register(SocialNetwork)
admin.site.register(SiteNavigation)
admin.site.register(FavoritesAndOther)
admin.site.register(Language)

admin.site.register(Chapter)
admin.site.register(Category)
admin.site.register(SubCategory)
