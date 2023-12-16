import pytest
from django.test import TestCase
from django.core.exceptions import ValidationError

from food.models import Food


# Create your tests here.

class FoodTests(TestCase):

    def setUp(self):
        ...

    def test_food_is_created(self):
        Food.objects.create(name='Pasta', price=850)
        pasta = Food.objects.get(name='Pasta')
        self.assertEqual(pasta.price, 850)

    def test_food_with_negative_price_throws_exception(self):
        food = Food(name='Food', price=-500)
        with pytest.raises(ValidationError):
            food.full_clean()

    def test_food_with_empty_name_throws_exception(self):
        food = Food(name='', price=100)
        with pytest.raises(ValidationError):
            food.full_clean()
