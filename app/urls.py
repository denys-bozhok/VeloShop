from django.urls import path

from .views import home, abouts, chapters, categories, subcategories


urlpatterns = [
    path('', home, name='index'),
    path('about/<slug:about_slug>/', abouts, name='about'),
    path('chapter/<slug:chapter_slug>/', chapters, name='chapters'),
    path('category/<slug:category_slug>/', categories, name='category'),
    path('category/<slug:category_slug>/<slug:subcategory_slug>/', subcategories, name='subcategories'),
    ]