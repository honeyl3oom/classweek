from django.test import TestCase
from django.core.exceptions import ValidationError

from classes.models import Category, SubCategory

class CategoryModelTest(TestCase):
    pass
    # def test_default_name(self):
    #     category = Category()
    #     self.assertEqual( category.name, '' )