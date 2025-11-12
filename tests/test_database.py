import sys
import os
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from database import Database
from data.data import Constants


class TestDataBase:

    @pytest.mark.parametrize("expexted_result, index", [
        ((Constants.bun_name_black_bun, 100), 0),
        ((Constants.bun_name_white_bun, 200), 1),
        ((Constants.bun_name_red_bun, 300), 2)
    ])
    def test_available_buns_buns_list_buns(self, expexted_result, index):
        database = Database()
        buns = database.available_buns()
        buns_list = (buns[index].name, buns[index].price)

        assert buns_list == expexted_result


    @pytest.mark.parametrize("expexted_result, index", [
        ((Constants.INGREDIENT_TYPE_SAUCE, Constants.ingredient_name_hot_sauce, 100), 0),
        ((Constants.INGREDIENT_TYPE_SAUCE, Constants.ingredient_name_sour_cream, 200), 1),
        ((Constants.INGREDIENT_TYPE_SAUCE, Constants.ingredient_name_chili_sauce, 300), 2),
        ((Constants.INGREDIENT_TYPE_FILLING, Constants.ingredient_name_cutlet, 100), 3),
        ((Constants.INGREDIENT_TYPE_FILLING, Constants.ingredient_name_dinosaur, 200), 4),
        ((Constants.INGREDIENT_TYPE_FILLING, Constants.ingredient_name_sausage, 300), 5),
    ])
    def test_available_ingredients_ingredients_list_ingredients(self, expexted_result, index):
        database = Database()
        ingredients = database.available_ingredients()
        ingredients_list = (ingredients[index].type, ingredients[index].name, ingredients[index].price)

        assert ingredients_list == expexted_result
