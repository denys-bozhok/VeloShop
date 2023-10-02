from django.urls import path

from .views import home, chapters, category


urlpatterns = [
    path('', home, name='index'),
    path('<slug:chapter_slug>', chapters, name='chapters'),
    path('<slug:chapter_slug>/<slug:category_slug>/', category, name='category'),]