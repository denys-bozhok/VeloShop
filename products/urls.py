from django.urls import path

from .views import card_of_product


urlpatterns = [
    path('<slug:slug>/', card_of_product, name='cart_of_product'),
    ]