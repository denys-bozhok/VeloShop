from queryset_sequence import QuerySetSequence

from .models import *


def all_products(req):
    bicycles = Bicycle.objects.all()
    accessories = Accessorie.objects.all()
    components = Component.objects.all()
    query_sets = QuerySetSequence(bicycles, accessories, components)

    return query_sets


def bicycles_filter(req):
    bicycles = Bicycle.objects.all()

    wheel = req.GET.get('wheel')
    size = req.GET.get('size')

    if size:
        size_id = Size.objects.get(short_name=size).id
        bicycles = bicycles.filter(frame_size=size_id)

    if wheel:
        wheel_id = WheelSize.objects.get(size=float(wheel)).id
        bicycles = bicycles.filter(wheel=wheel_id)

    return bicycles


def filters(req, model_name):
    match(model_name):
        case 'Bicycles':
            products = bicycles_filter(req)
            return products

        case 'Accessories':
            products = bicycles_filter(req)
            return products
