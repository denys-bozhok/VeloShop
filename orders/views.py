from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from .forms import OrderCreateForm
from .models import Order

app_name = 'orders'


class OrderCreateView(CreateView):
    template_name = 'orders/includes/_order_create.html'
    form_class = OrderCreateForm


class OrdersList(ListView):
    model = Order
    template_name = 'orders/includes/_orders.html'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/includes/_order_info.html'


def order_create_success_view(req):
    context = {'title': 'Success'}

    return render(req, 'orders/orders.html', context)



