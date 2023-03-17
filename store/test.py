from django.test import TestCase
from .models import Category

class TestCreateInstance(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name = 'Fiction',
            slug = 'fiction'
        )
        self.category.save()

    def test_is_instance_created(self):
        get_instance = Category.objects.get(name='Fiction')
        self.assertEqual(get_instance.name, self.category.name)
        self.assertEqual(get_instance.slug, self.category.slug)
        self.assertIsInstance(self.category, Category)

    def tearDown(self):
        Category.objects.all().delete()