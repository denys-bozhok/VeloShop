from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Cart
from .forms import QuantityUpdateView
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
    try:
        cart_items = Cart.objects.filter(user=req.user)
    except:
        cart_items = Cart.objects.filter(id=0)

    total_cost = 0

    products = []

    for item in cart_items:
        product_quantity = item.quantity

        for product in all_products().filter(article=item.product):
            products_cost = product.price * product_quantity
            total_cost += products_cost

            product_data = {
                'cart_id': item.id,
                'product_quantity': product_quantity,
                'products_cost': products_cost,
                'product': product,
                'item': item
            }

        products.append(product_data)

    context = {
        "cart_items": cart_items,
        "total_cost": total_cost,
        'products': products
    }

    return render(req, "carts/carts.html", context)


@login_required
def edit_quantity(req: object, cart_id: int) -> classmethod:
    cart = Cart.objects.get(id=cart_id)

    if req.method == 'POST':
        form = QuantityUpdateView(instance=cart, data=req.POST)
        cart.quantity = req.POST['quantity']
        if cart.quantity == 0:
            cart.delete()
        else:
            cart.save()
            return HttpResponseRedirect(reverse('carts:cart_detail'))
    else:
        form = QuantityUpdateView(instance=cart)

    context = {'form': form,
               'cart': cart}

    return render(req, 'carts/includes/_quantity_update.html', context)
