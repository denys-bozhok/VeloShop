from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
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
    cart_products = []
    total = 0

    for item in cart_items:

        for product in ProductsQuerySet.all_products(''):
            if product.article == item.product:
                product_sum = product.price * item.quantity
                total += product_sum
                    
                product_data = {'quantity': item.quantity,
                                "item_id": item.id,
                                'product': product,
                                'product_sum': product_sum}

                cart_products.append(product_data)

    context = {
        'cart_products': cart_products,
        'total': total,
    }

    return render(req, "carts/includes/_cart_detail.html", context)

