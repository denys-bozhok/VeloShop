from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import *
from .models import Cart


@login_required
def add_to_cart(req, article):
    cart_item = Cart.objects.filter(user=req.user, product=article).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(req, "Item added to your cart.")
    else:
        Cart.objects.create(user=req.user, product=article)
        messages.success(req, "Item added to your cart.")

    return redirect("carts:cart_detail")


@login_required
def remove_from_cart(req, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)

    if cart_item.user == req.user:
        cart_item.delete()
        messages.success(req, "Item removed from your cart.")

    return redirect("carts:cart_detail")


@login_required
def cart_detail(req):
    cart_items = Cart.objects.filter(user=req.user)
    products = []
    total_price = 0

    for item in cart_items:
        for proruct in ProductsQuerySet.all_products(''):
            if proruct.article == item.product:
                prices = proruct.price * item.quantity
                total_price += prices
                
                product_data = {'quantity': item.quantity,
                                'product': proruct,
                                'prices': prices}
                
                products.append(product_data)

    context = {
        'products': products,
        'total_price': total_price
    }

    return render(req, "carts/includes/_cart_detail.html", context)

