from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.conf import settings
from django.http import HttpResponseRedirect
import stripe
from django.views.generic.base import TemplateView

from .forms import OrderCreateForm
from .models import Order
from common.views import TitleMixin
from carts.models import Cart

app_name = 'orders'

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessTemplateView(TitleMixin, TemplateView):
    template_name = 'orders/orders.html'
    title = 'Success'


class CanceledTemplateView(TitleMixin, TemplateView):
    template_name = 'orders/includes/_success.html'
    title = 'Cancel'


class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/orders.html'
    form_class = OrderCreateForm
    success_url = reverse_lazy('order_success')
    title = 'New Order'

    def post(self, req, *args, **kwargs):
        super(OrderCreateView, self).post(req, *args, **kwargs)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1OvVguA382WBKVuqaiWE4qE0',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url = '{}{}'.format(settings.DOMAIN_NAME, reverse('order_success')),
            cancel_url = '{}{}'.format(settings.DOMAIN_NAME, reverse('order_cancel')),
        )
        return HttpResponseRedirect(checkout_session.url, status=303)
        

    def form_valid(self, form):
        carts = Cart.objects.filter(user=self.request.user)
        form.instance.user = self.request.user
        
        for cart in carts:
            form.instance.order_info += (cart.product for cart in Cart.objects.filter(user=self.request.user).order_by('id'))
            cart.delete()

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

