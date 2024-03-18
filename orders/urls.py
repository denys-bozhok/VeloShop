from django.urls import path

from .views import OrderCreateView, OrdersList, OrderDetailView, order_create_success_view, SuccessTemplateView, CanceledTemplateView


urlpatterns = [
    path('<int:id>/', OrdersList.as_view(), name='users_orders'),
    path('details/<int:id>/', OrderDetailView.as_view(), name='order_detail'),
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('success/', SuccessTemplateView.as_view(), name='order_success'),
    path('cancel/', CanceledTemplateView.as_view(), name='order_cancel'),
    ]