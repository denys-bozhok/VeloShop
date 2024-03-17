from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import OrderCreateForm
from .models import Order
from common.views import TitleMixin


app_name = 'orders'


class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/orders.html'
    form_class = OrderCreateForm
    success_url = reverse_lazy('order_success')
    title = 'New Order'

    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super(OrderCreateView, self).form_valid(form)
    

class OrdersList(ListView):
    model = Order
    template_name = 'orders/includes/_orders.html'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/includes/_order_info.html'


def order_create_success_view(req):
    context = {'title': 'Success'}

    return render(req, 'orders/orders.html', context)



