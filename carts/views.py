from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from app import utilites
from .models import Cart
from .forms import CartQuantityUpdateForm
from products.filters import filters


@login_required
def add_to_cart(req, article):
    product = filters(req).get(article=article)

    product_data = {
        'label': product.label,
        'article': product.article,
        'price': float(product.price),
    }

    cart = Cart.objects.filter(user=req.user, product=product_data).first()

    if cart:
        cart.quantity += 1
        cart.save()
        messages.success(req, "Item added to your cart.")
    else:
        Cart.objects.create(user=req.user, product=product_data)
        messages.success(req, "Item added to your cart.")

    return redirect("carts:cart_detail")


@login_required
def remove_from_cart(req, id):
    cart = get_object_or_404(Cart, id=id)

    if cart.user == req.user:
        cart.delete()
        messages.success(req, "Item removed from your cart.")

    return redirect("carts:cart_detail")


@login_required
def cart_detail(req):
    cart_sum = 0
    products = []

    try:
        carts = Cart.objects.filter(user=req.user).order_by('id')
    except:
        carts = Cart.objects.filter(id=0)

    for cart in carts:
        if cart.quantity != 0:
            cart_sum += cart.quantity * cart.product['price']
            products.append({
                'form': CartQuantityUpdateForm(instance=cart),
                'cart_id': cart.id,
                'product_sum': cart.quantity * cart.product['price'],
                'product_quantity': cart.quantity,
                'product': filters(req).get(article=cart.product['article']),
                })

    context = {'cart_sum': cart_sum, 'products': products}

    context.update(utilites.subheader(req))

    return render(req, "carts/carts.html", context)


@login_required
def edit_quantity(req: object, cart_id: int) -> classmethod:
    cart = Cart.objects.get(id=cart_id).order_by('id')

    if req.method == 'POST':
        form = CartQuantityUpdateForm(instance=cart, data=req.POST)
        cart.quantity = req.POST['quantity']
        if cart.quantity == 0:
            cart.delete()
        else:
            cart.save()
            return HttpResponseRedirect(reverse('carts:cart_detail'))



