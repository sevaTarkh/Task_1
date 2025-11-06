import sys
import os
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from burger import Burger
from data.data import Constants
from unittest.mock import Mock

class TestBurger:


    def test_set_buns_bun_get_bun(self):
        burger = Burger()

        burger.set_buns(Constants.bun_name_classic)
        assert burger.bun == Constants.bun_name_classic

    def test_add_ingredient_ingredient_list_ingredients(self):
        burger = Burger()

        burger.add_ingredient(Constants.ingredient_name_bbq)

        assert burger.ingredients == [Constants.ingredient_name_bbq]

    def test_remove_ingredient_index_new_list(self):
        burger = Burger()

        burger.add_ingredient(Constants.ingredient_name_bbq)
        burger.add_ingredient(Constants.ingredient_name_cheese)

        burger.remove_ingredient(0)

        assert burger.ingredients == [Constants.ingredient_name_cheese]

    def test_move_ingredient_index_new_index(self):
        burger = Burger()

        burger.add_ingredient(Constants.ingredient_name_bbq)
        burger.add_ingredient(Constants.ingredient_name_cheese)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [Constants.ingredient_name_cheese, Constants.ingredient_name_bbq]

    @pytest.mark.parametrize('bun_price, ingredient_1_price, ingredient_2_price, expected_price', [
        (50.0, 20.0, 25.0, 145.0),
        (40.0, 20.0, 15.0, 115.0),
        (65.0, 50.0, 20.0, 200.0)
    ])
    def test_get_price_prices_burger_price(self, bun_price, ingredient_1_price, ingredient_2_price, expected_price):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = ingredient_1_price
        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = ingredient_2_price
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        result = burger.get_price()

        assert result == expected_price

    @pytest.mark.parametrize("bun_name, ingredient_1_type, ingredient_1_name, ingredient_2_type, ingredient_2_name, bun_price, ingredient_1_price, ingredient_2_price, expected_result",[
        (Constants.bun_name_classic, Constants.ingredient_type_bacon, Constants.ingredient_name_cheese, Constants.ingredient_type_sauce, Constants.ingredient_name_sour, 50, 25, 25, [
            f'(==== {Constants.bun_name_classic} ====)',
            f'= {Constants.ingredient_type_bacon.lower()} {Constants.ingredient_name_cheese } =',
            f'= {Constants.ingredient_type_sauce.lower()} {Constants.ingredient_name_sour} =',
            f'(==== {Constants.bun_name_classic} ====)',
            '',
            'Price: 150'
        ]),
        (Constants.bun_name_dark, Constants.ingredient_type_tomatoes, Constants.ingredient_name_mustard, Constants.ingredient_type_cheese, Constants.ingredient_name_sour, 100, 50, 30, [
            f'(==== {Constants.bun_name_dark} ====)',
            f'= {Constants.ingredient_type_tomatoes.lower()} {Constants.ingredient_name_mustard } =',
            f'= {Constants.ingredient_type_cheese.lower()} {Constants.ingredient_name_sour} =',
            f'(==== {Constants.bun_name_dark} ====)',
            '',
            'Price: 280'
        ])
    ])
    def test_get_receipt_receipt(self, bun_name, ingredient_1_type, ingredient_1_name, ingredient_2_type, ingredient_2_name, bun_price, ingredient_1_price, ingredient_2_price, expected_result):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = bun_name
        mock_bun.get_price.return_value = bun_price

        mock_ingredient1 = Mock()
        mock_ingredient1.get_type.return_value = ingredient_1_type
        mock_ingredient1.get_name.return_value = ingredient_1_name
        mock_ingredient1.get_price.return_value = ingredient_1_price

        mock_ingredient2 = Mock()
        mock_ingredient2.get_type.return_value = ingredient_2_type
        mock_ingredient2.get_name.return_value = ingredient_2_name
        mock_ingredient2.get_price.return_value = ingredient_2_price

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        expected_receipt = "\n".join(expected_result)

        assert burger.get_receipt() == expected_receipt
