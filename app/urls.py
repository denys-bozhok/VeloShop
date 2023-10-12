from django.urls import path

from .views import home, about, chapters, category, subcategory


urlpatterns = [
    path('', home, name='index'),
    path('about/<slug:about_slug>/', about, name='about'),
    path('<slug:chapter_slug>/', chapters, name='chapters'),
    path('category/<slug:category_slug>/', category, name='category'),
    path('category/<slug:category_slug>/<slug:subcategory_slug>/', subcategory, name='subcategory'),
    ]