import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import conftest
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.select_sticker import SelectSticker
from pages.shopping_cart_page import ShoppingCartPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.buyAngryScene2

class TestBuyAngry:
    def test_buy_angry(self):
        driver = conftest.driver
        home_page = HomePage()
        select_sticker = SelectSticker()
        go_to_cart_page = ShoppingCartPage()
        verify_products = ShoppingCartPage()
        complete_checkout = CheckoutPage()

        #open Stickerfy page.
        home_page.successful_login()

        # select Happy sticker clicking in Add to cart blue button.
        select_sticker.sticker_angry()

        # go to cart page.
        go_to_cart_page.click_shopping_cart_button()

        # verification of Happy Sticker into cart page.
        verify_products.verify_angry()

        # click on checkout and confirm checkout.
        complete_checkout.full_checkout_page()
