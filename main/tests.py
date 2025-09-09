from django.test import TestCase, Client
from .models import Product

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/burhan_always_exists/')
        self.assertEqual(response.status_code, 404)

    def test_product_creation(self):
        product = Product.objects.create(
          name = "Barcelona 2025 Jersey",
          price = 999000,
          description = "Barcelona New 2025 Jersey",
          category = "jersey",
          is_featured = True,
          product_views = 1000000
        )
        self.assertTrue(product.is_booming_product)
        self.assertEqual(product.category, "jersey")
        self.assertTrue(product.is_featured)
        
    def test_product_default_values(self):
        product = Product.objects.create(
          name = "Test Product",
          description = "Test description"
        )
        self.assertEqual(product.product_views, 0)
        self.assertFalse(product.is_featured)
        self.assertFalse(product.is_booming_product)
        
    def test_increment_views(self):
        product = Product.objects.create(
          name = "Test Product",
          description = "Test description"
        )
        initial_views = product.product_views
        product.increment_views()
        self.assertEqual(product.product_views, initial_views + 1)
        
    def test_is_product_hot_threshold(self):
        # Test product with exactly 20 views (should not be hot)
        product_20 = Product.objects.create(
          name = "Product with 20000 views",
          description = "Test description",
          product_views = 20000
        )
        self.assertFalse(product_20.is_booming_product)
        
        # Test product with 21 views (should be hot)
        product_21 = Product.objects.create(
          name = "Product with 21000 views", 
          description = "Test description",
          product_views = 21000
        )
        self.assertTrue(product_21.is_booming_product)