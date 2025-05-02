import pytest

import conftest
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.select_sticker import SelectSticker
from pages.shopping_cart_page import ShoppingCartPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.buyNothing

class TestBuyNothing:
    def test_buy_happy(self):
        driver = conftest.driver
        home_page = HomePage()
        go_to_cart_page = ShoppingCartPage()
        empty_checkout = CheckoutPage()

        #open Stickerfy page.
        home_page.successful_login()

        #go to cart page.
        go_to_cart_page.click_go_to_cart_button()

        #click on checkout and confirm checkout.
        empty_checkout.empty_checkout_page()