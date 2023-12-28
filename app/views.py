from django.shortcuts import render

from .models import SiteNavigation, Chapter, Category, SubCategory
from .utilites import subheader, for_categories


def home(req: object) -> classmethod:
    context = {'title': 'VeloShop', 'chapters': Chapter.objects.all()}
    context.update(subheader(req))

    return render(req, 'app/app.html', context)


def abouts(req: object, about_slug: str) -> classmethod:
    about = SiteNavigation.objects.get(slug=about_slug)
    context = {'title': about.name, 'about': about}
    context.update(subheader(req))

    return render(req, 'app/app.html', context)


def chapters(req: object, chapter_slug: str) -> classmethod:
    context = for_categories(req, chapter_slug, Chapter)
    context.update(subheader(req))

    return render(req, 'app/app.html', context)


def categories(req: object, category_slug: str) -> classmethod:
    context = for_categories(req, category_slug, Category)
    context.update(subheader(req))

    return render(req, 'app/app.html', context)


def sub_categories(req: object, category_slug: str, sub_category_slug: str) -> classmethod:
    context = for_categories(req,
                             sub_category_slug, SubCategory, category_slug)
    context.update(subheader(req))
    return render(req, 'app/app.html', context)
