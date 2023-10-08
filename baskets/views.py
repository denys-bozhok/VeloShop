from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from products.models import Bicycle
from .models import Basket


@login_required
def basket_add(req, slug):
    product = Bicycle.objects.get(slug=slug)
    baskets = Basket.objects.filter(user=req.user, product=product)

    if not basket.exists:
        Basket.objects.create(user=req.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    
    return HttpResponseRedirect(req.META['HTTP_REFERER'])

@login_required
def basket_remove(req, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    
    return HttpResponseRedirect(req.META['HTTP_REFERER'])