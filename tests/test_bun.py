import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from bun import Bun
from data.data import Constants
import pytest


class TestBun:

    @pytest.mark.parametrize("bun_name", [
        Constants.bun_name_with_sesame_seeds,
        Constants.bun_name_dark,
        Constants.bun_name_classic,
        '',
    ])
    def test_get_name_bun_name_return_bun_name(self, bun_name):
        bun = Bun(bun_name, 60)
        assert bun.get_name() == bun_name


    @pytest.mark.parametrize("bun_price", [
        123.12,
        66.0,
        0,
    ])
    def test_get_price_bun_price_return_bun_price(self, bun_price):
        bun = Bun(Constants.bun_name_classic, bun_price)
        assert bun.get_price() == bun_price
