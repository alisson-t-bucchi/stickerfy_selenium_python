import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import conftest
from pages.home_page import HomePage
from pages.select_sticker import SelectSticker
from pages.shopping_cart_page import ShoppingCartPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.buyAllStickersScene2
class TestBuyAllStickers:

    def test_buy_all_stickers(self):
        driver = conftest.driver
        select_sticker = SelectSticker()
        buy_2_stickers = SelectSticker()
        home_page = HomePage()
        go_to_cart_page = ShoppingCartPage()
        verify_products = ShoppingCartPage()

        #open page and find Stickerfy title
        #assert driver.find_element(By.XPATH, "//a[@class='navbar-brand' and text()='Stickerfy']").is_displayed()
        home_page.successful_login()


        #select all stickers
        #driver.find_element(By.XPATH, "//a[@href='/add-to-cart/5dd8e2b26c26d0000a675cf9']").click()
        #driver.find_element(By.XPATH, "//a[@href='/add-to-cart/5dd8e2b26c26d0000a675cfa']").click()
        #driver.find_element(By.XPATH, "//a[@href='/add-to-cart/5dd8e2b26c26d0000a675cfb']").click()
        select_sticker.all_stickers()

        #buy_2_stickers.select_2_happy()

        #click on "Go to cart" button
        #driver.find_element(By.XPATH, "//a[@href='/shopping-cart/' and text()='Go to cart']").click()
        go_to_cart_page.click_shopping_cart_button()
        verify_products.verify_all_stickers()

        #wait = WebDriverWait(driver, 5)
        #wait.until(EC.presence_of_element_located((By.XPATH, "//strong[text()='Total: 17']"))

        #click on checkout
        driver.find_element(By.XPATH, "//a[@href='/checkout' and text()='Checkout']").click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, "//h4[text()='Thanks for your order!']")))



