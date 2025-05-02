import time
import pytest

import conftest
from pages.home_page import HomePage
from pages.select_sticker import SelectSticker
from pages.shopping_cart_page import ShoppingCartPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.removeAllForEachSticker
class TestRemoveAllForEachSticker:

    def test_remove_all_for_each_sticker(self):
        driver = conftest.driver
        home_page = HomePage()
        select_sticker = SelectSticker()
        go_to_cart_page = ShoppingCartPage()
        click_on_and_remove_all = ShoppingCartPage()
        empty_cart_page = ShoppingCartPage()

        home_page.successful_login()

        select_sticker.all_stickers()

        go_to_cart_page.click_go_to_cart_button()

        click_on_and_remove_all.click_on_and_remove_all_each_sticker()

        empty_cart_page.empty_page()



#Formas de encontrar o botão dentro do box que contem a palavra Happy:
#//li[strong/text()='Happy']//button
#"//li[contains(., 'Happy')]//button")