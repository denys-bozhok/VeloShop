from django.urls import path

from .views import OrderCreateView, OrdersList, OrderDetailView, order_create_success_view


urlpatterns = [
    path('<int:id>/', OrdersList.as_view(), name='users_orders'),
    path('details/<int:id>/', OrderDetailView.as_view(), name='order_detail'),
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('success/', order_create_success_view, name='order_success'),
    ]