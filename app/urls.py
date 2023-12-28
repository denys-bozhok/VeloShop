from django.urls import path

from .views import home, abouts, chapters, categories, sub_categories


urlpatterns = [
    path('', home, name='index'),
    path('about/<slug:about_slug>/', abouts, name='about'),
    path('chapter/<slug:chapter_slug>/', chapters, name='chapter'),
    path('category/<slug:category_slug>/', categories, name='category'),
    path('category/<slug:category_slug>/<slug:sub_category_slug>/',
         sub_categories, name='sub_categories'),
]
