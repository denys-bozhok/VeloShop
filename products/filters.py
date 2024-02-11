from queryset_sequence import QuerySetSequence

from .models import Bicycle, BicycleGalery, Accessorie, AccessorieGalery, Component, ComponentGalery


def all_products():

    bicycle = Bicycle.objects.all()
    accessories = Accessorie.objects.all()
    components = Component.objects.all()

    query_sets = QuerySetSequence(bicycle, accessories, components)

    return query_sets
