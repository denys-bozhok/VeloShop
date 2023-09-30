from django.urls import path

from .views import home, sass


urlpatterns = [
    path('', home, name='index'),
    ]