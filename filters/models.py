from django.db import models

from products.models import Bicycle, BicycleGalery, Accessorie, AccessorieGalery, Component, ComponentGalery

from queryset_sequence import QuerySetSequence


class ProductFilter(models.QuerySet):
    def all_products():
        return QuerySetSequence(Bicycle.objects.all(), Accessorie.objects.all(), Component.objects.all())

    def product_filter_by_category(category: object):
        try:
            return QuerySetSequence(
                Bicycle.objects.filter(category=category),
                Accessorie.objects.filter(category=category),
                Component.objects.filter(category=category))

        except:
            return QuerySetSequence(
                Bicycle.objects.filter(subcategory=category),
                Accessorie.objects.filter(subcategory=category),
                Component.objects.filter(subcategory=category))

    def filter_options(req: object):
        return {
            'wheel': req.GET.get('wheel'),
            'price': req.GET.get('price'),
            'suspension': req.GET.get('suspension'),
            'year': req.GET.get('year'),
            'material': req.GET.get('material'),
            'rating': req.GET.get('rating'),
            'manufakturer': req.GET.get('manufakturer'),
            'frame': req.GET.get('frame'),
            'weigth': req.GET.get('weigth'),
        }

    def filter_products(req, *args):
        filtred_products = []
        products = args[0]

        filter_options = ProductFilter.filter_options(req)

        wheel = filter_options['wheel']
        year = filter_options['year']
        rating = filter_options['rating']
        frame = filter_options['frame']
        price = filter_options['price']
        suspension = filter_options['suspension']
        material = filter_options['material']
        manufakturer = filter_options['manufakturer']

        for product in products:
            if product.wheel.__str__() == wheel:
                filtred_products.append(product)
            if product.rating.__str__() == rating:
                filtred_products.append(product)
            if product.year.__str__() == year:
                filtred_products.append(product)
            if product.frame_size.__str__() == frame:
                filtred_products.append(product)
            # if product.price.__str__() == price:
            #     filtred_products.append(product)
            # if product.suspension.__str__() == suspension:
            #     filtred_products.append(product)
            # if product.frame_material.__str__() == material:
            #     filtred_products.append(product)
            # if product.manufakturer.__str__() == manufakturer:
            #     filtred_products.append(product)

        for filtred_product in filtred_products:
            if rating:
                if filtred_product.rating.__str__() != rating:
                    filtred_products.remove(filtred_product)
            if wheel:
                if filtred_product.wheel.__str__() != wheel:
                    filtred_products.remove(filtred_product)
            if year:
                if filtred_product.year.__str__() != year:
                    filtred_products.remove(filtred_product)

            if frame:
                if filtred_product.frame_size.__str__() != frame:
                    filtred_products.remove(filtred_product)
            # if price:
            #     if filtred_product.price.__str__() != price:
            #         filtred_products.remove(filtred_product)

            # if suspension:
            #     if filtred_product.suspension.__str__() != suspension:
            #         filtred_products.remove(filtred_product)

            # if material:
            #     if filtred_product.frame_material.__str__() != material:
            #         filtred_products.remove(filtred_product)

            # if manufakturer:
            #     if filtred_product.manufakturer.__str__() != manufakturer:
            #         filtred_products.remove(filtred_product)

        filtred_products = list(set(filtred_products))

        if filtred_products != []:
            products = QuerySetSequence(filtred_products, )

        return products
