import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from typing import List

from bun import Bun
from ingredient import Ingredient
from data.data import Constants

class Database:
    """
    Класс с методами по работе с базой данных.
    """

    def __init__(self):
        self.buns: List[Bun] = []
        self.ingredients: List[Ingredient] = []

        self.buns.append(Bun(Constants.bun_name_black_bun, 100))
        self.buns.append(Bun(Constants.bun_name_white_bun, 200))
        self.buns.append(Bun(Constants.bun_name_red_bun, 300))

        self.ingredients.append(Ingredient(Constants.INGREDIENT_TYPE_SAUCE, Constants.ingredient_name_hot_sauce, 100))
        self.ingredients.append(Ingredient(Constants.INGREDIENT_TYPE_SAUCE, Constants.ingredient_name_sour_cream, 200))
        self.ingredients.append(Ingredient(Constants.INGREDIENT_TYPE_SAUCE, Constants.ingredient_name_chili_sauce, 300))

        self.ingredients.append(Ingredient(Constants.INGREDIENT_TYPE_FILLING, Constants.ingredient_name_cutlet, 100))
        self.ingredients.append(Ingredient(Constants.INGREDIENT_TYPE_FILLING, Constants.ingredient_name_dinosaur, 200))
        self.ingredients.append(Ingredient(Constants.INGREDIENT_TYPE_FILLING, Constants.ingredient_name_sausage, 300))

    def available_buns(self) -> List[Bun]:
        return self.buns

    def available_ingredients(self) -> List[Ingredient]:
        return self.ingredients
