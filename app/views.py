from django.shortcuts import render

from .models import SiteNavigation, Chapter, CharterQuerySet, Category, SubCategory
from .utilites import subheader, for_categories



def home(req:object) -> classmethod:
    context = {'title': 'VeloShop', 'chapters': CharterQuerySet.all_models(Chapter)}
    context.update(subheader())

    return render(req, 'app/app.html', context)


def abouts(req:object, about_slug:str) -> classmethod:
    about = CharterQuerySet.model_by_slug(SiteNavigation, about_slug)
    context = {'title': about.name, 'about':about}
    context.update(subheader())

    return render(req, 'app/app.html', context)


def chapters(req:object, chapter_slug:str) -> classmethod:
    context = for_categories(chapter_slug, Chapter)
    context.update(subheader())

    return render(req, 'app/app.html', context)


def categories(req:object, category_slug:str, ) -> classmethod:
    context = for_categories(category_slug, Category)
    context.update(subheader())

    return render(req, 'app/app.html', context)


def subcategories(req:object, category_slug, subcategory_slug) -> classmethod:
    context = for_categories(subcategory_slug, SubCategory)
    context.update(subheader())

    return render(req, 'app/app.html', context)