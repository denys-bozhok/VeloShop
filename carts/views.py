from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import *
from app import utilites
from .forms import EditProductSumForm
from .models import Cart
from .utilites import for_cart_detail


@login_required
def cart_detail(req:object) -> classmethod:
    title = 'Cart'
    context = {'title': title}
    context.update(for_cart_detail(req))
    context.update(utilites.subheader(req))

    return render(req, "carts/carts.html", context)


@login_required
def add_to_cart(req:object, article:str) -> classmethod:
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
def remove_from_cart(req:object, cart_item_id:int) -> classmethod:
    cart_item = get_object_or_404(Cart, id=cart_item_id)

    if cart_item.user == req.user:
        cart_item.delete()
        messages.success(req, "Item removed from your cart.")

    return redirect("carts:cart_detail")


@login_required
def edit_product_sum(req:object, id:int) -> classmethod:
    cart = Cart.objects.get(id=id)
    
    if req.method == 'POST':
        form_for_quantity = EditProductSumForm(instance=cart, data=req.POST)
        cart.quantity = req.POST['quantity']
        if cart.quantity == 0:
            cart.delete()
        else:
            cart.save()
            return HttpResponseRedirect(reverse('carts:cart_detail'))
    else:
        form_for_quantity = EditProductSumForm(instance=cart)
        
    context = {'form_for_quantity': form_for_quantity, 
               'cart': cart}

    return render(req, 'carts/includes/_edit_quantity.html', context)