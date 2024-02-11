from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart
from products.filters import all_products


@login_required
def add_to_cart(req, article):
    cart_item = Cart.objects.filter(
        user=req.user, product=article).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(req, "Item added to your cart.")
    else:
        Cart.objects.create(user=req.user, product=article)
        messages.success(req, "Item added to your cart.")

    return redirect("carts:cart_detail")


@login_required
def remove_from_cart(req, id):
    cart_item = get_object_or_404(Cart, id=id)

    if cart_item.user == req.user:
        cart_item.delete()
        messages.success(req, "Item removed from your cart.")

    return redirect("carts:cart_detail")


@login_required
def cart_detail(req):
    cart_items = Cart.objects.filter(user=req.user)
    total_price = 0

    for cart in cart_items:
        total_price += all_products().get(article=cart.product).price

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }

    return render(req, "carts/carts.html", context)
