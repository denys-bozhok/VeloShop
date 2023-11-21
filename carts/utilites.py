from products.models import *
from .models import Cart


def for_cart_detail(req:object) -> dict:
    try:
        cart_items = Cart.objects.filter(user=req.user)
    except:
        cart_items = Cart.objects.filter(id=0)

    cart_products = []
    total = 0
    items_quantity = 0

    for item in cart_items:

        for product in ProductsQuerySet.all_products(''):
            if product.article == item.product and item.quantity != 0:
                items_quantity += item.quantity
                product_sum = product.price * item.quantity
                total += product_sum
                    
                product_data = {'quantity': item.quantity,
                                "item_id": item.id,
                                'product': product,
                                'product_sum': product_sum}

                cart_products.append(product_data)


    return {'cart_products': cart_products, 'total': total, 'items_quantity': items_quantity}
