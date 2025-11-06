import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from ingredient import Ingredient
from data.data import Constants
import pytest

class TestIngredient:

    @pytest.mark.parametrize("ingredient_price", [
        20.5,
        13.8,
        0,
        123.7
    ])
    def test_get_price_ingridient_price_return_price(self, ingredient_price):
        ingredient = Ingredient(
            Constants.ingredient_type_sauce,
            Constants.ingredient_name_cheese,
            ingredient_price
        )
        assert ingredient.get_price() == ingredient_price

    @pytest.mark.parametrize("ingredient_name", [
        Constants.ingredient_name_bbq,
        Constants.ingredient_name_cheese,
        Constants.ingredient_name_sour,
        Constants.ingredient_name_mustard,
    ])
    def test_get_name_ingridient_name_return_name(self, ingredient_name):
        ingredient = Ingredient(Constants.ingredient_type_sauce, ingredient_name, 50)
        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize("ingredient_type", [
        Constants.ingredient_type_sauce,
        Constants.ingredient_type_tomatoes,
        Constants.ingredient_type_cheese,
        Constants.ingredient_type_bacon, 
    ])   
    def test_get_type_ingridient_type_return_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, Constants.ingredient_name_cheese, 50)
        assert ingredient.get_type() == ingredient_type