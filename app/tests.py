from django.test import TestCase
from django.urls import reverse

from users.models import User
from app.models import *
from products.models import *


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['title'], 'VeloShop')
        self.assertTemplateUsed(response, 'app/app.html')

class ProductListViewTestCase(TestCase):
    fixtures = ['chapters.json', 
                'categories.json', 
                'bicycles.json', 
                'mat.json', 
                'frame.json', 
                'manufacturers.json', 
                'sub_category.json',
                'suspension_travels.json',
                'weights.json',
                'wheels.json',
                'characteristics.json',
                'characteristic_values.json',
                'colors.json',
                ]

    def test_list(self):
        chapters = Chapter.objects.all()
        bicycles = Bicycle.objects.all()
        categories = Category.objects.all()

        for chapter in chapters:
            path = reverse('chapter', kwargs={'chapter_slug': chapter.slug})
            response = self.client.get(path)

            for category in categories.filter(chapter=chapter):
                
                for bicycle in bicycles.filter(category=category):
                    bicycle_path = reverse('cart_of_product', kwargs={'slug': bicycle.slug})
                    bicycle_response = self.client.get(bicycle_path)

                    self.assertEqual(bicycle_response.status_code, 200)
                    self.assertTemplateUsed(bicycle_response, 
                                            'products/includes/_card_of_product.html')

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.context['title'], chapter.name)
        

