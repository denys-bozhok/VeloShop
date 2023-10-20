from django.urls import path
from . import views

app_name = "carts"

urlpatterns = [
    path('add/<str:article>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('', views.cart_detail, name='cart_detail'),
]