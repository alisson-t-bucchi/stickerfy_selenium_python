import time

import pytest

import conftest
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.select_sticker import SelectSticker
from pages.shopping_cart_page import ShoppingCartPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.buyTwoOfEachStickerScene2
class TestBuyTwoOfEachSticker:

    def test_buy_all_stickers(self):
        driver = conftest.driver
        buy_2_of_each_stickers = SelectSticker()
        home_page = HomePage()
        go_to_cart_page = ShoppingCartPage()
        verify_products = ShoppingCartPage()
        complete_checkout = CheckoutPage()

        home_page.successful_login()

        buy_2_of_each_stickers.select_2_of_each_sticker()

        go_to_cart_page.click_shopping_cart_button()

        verify_products.verify_all_stickers()

        complete_checkout.full_checkout_page()


