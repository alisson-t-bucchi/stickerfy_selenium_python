import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import conftest
from pages.home_page import HomePage
from pages.select_sticker import SelectSticker
from pages.shopping_cart_page import ShoppingCartPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.removeOneForEachSticker
class TestRemoveOneForEachSticker:

    def test_remove_one_for_each_sticker(self):
        driver = conftest.driver
        home_page = HomePage()
        select_sticker = SelectSticker()
        go_to_cart_page = ShoppingCartPage()
        click_on_and_remove_1 = ShoppingCartPage()
        empty_cart_page = ShoppingCartPage()

        home_page.successful_login()

        select_sticker.all_stickers()

        go_to_cart_page.click_go_to_cart_button()

        click_on_and_remove_1.click_on_and_remove_1_each_sticker()

        empty_cart_page.empty_page()



#Formas de encontrar o botão dentro do box que contem a palavra Happy:
#//li[strong/text()='Happy']//button
#"//li[contains(., 'Happy')]//button")