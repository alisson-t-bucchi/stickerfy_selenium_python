import pytest

import conftest
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.select_sticker import SelectSticker
from pages.shopping_cart_page import ShoppingCartPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.buySadScene1

class TestBuySad:
    def test_buy_sad(self):
        driver = conftest.driver
        home_page = HomePage()
        select_sticker = SelectSticker()
        go_to_cart_page = ShoppingCartPage()
        verify_products = ShoppingCartPage()
        complete_checkout = CheckoutPage()

        #open Stickerfy page.
        home_page.successful_login()

        #select Happy sticker clicking in Add to cart blue button.
        select_sticker.sticker_sad()

        #go to cart page.
        go_to_cart_page.click_go_to_cart_button()

        #verification of Happy Sticker into cart page.
        verify_products.verify_sad()

        #click on checkout and confirm checkout.
        complete_checkout.full_checkout_page()