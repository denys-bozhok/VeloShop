from django.urls import path

from .views import basket_add, basket_remove


urlpatterns = [
    path('add/<slug:slug>/', basket_add, name='basket_add'),
    path('remove/<slug:slug>/', basket_remove, name='basket_remove'),
    ]