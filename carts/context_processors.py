from carts.models import Cart


# make global Peremennaya
def get_all_carts(req):
    user = req.user

    return {'carts': Cart.objects.filter(user=user).order_by('id') if user.is_authenticated else []}