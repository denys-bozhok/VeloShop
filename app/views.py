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


def chapters(req: object, chapter_slug: str, *page_number: int) -> classmethod:
    context = for_categories(chapter_slug, Chapter, page_number)
    context.update(subheader(req))

    return render(req, 'app/app.html', context)


def categories(req: object, category_slug: str, page: int = 1) -> classmethod:
    context = for_categories(category_slug, Category, page)
    context.update(subheader(req))

    return render(req, 'app/app.html', context)


def sub_categories(req: object, category_slug: str, sub_category_slug: str, page: int = 1) -> classmethod:
    context = for_categories(
        sub_category_slug, SubCategory, category_slug, page)
    context.update(subheader(req))
    return render(req, 'app/app.html', context)
