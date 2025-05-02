import time
import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ShoppingCartPage(BasePage):
    def __init__(self): #construtor da classe
        self.driver = conftest.driver
        self.go_to_cart_button = (By.XPATH, "//a[@href='/shopping-cart/' and text()='Go to cart']")
        self.shopping_cart_button = (By.XPATH, "//span[@class='badge']")
        self.have_happy = (By.XPATH, "//li[contains(., 'Happy')]//button")
        self.have_sad = (By.XPATH, "//li[contains(., 'Sad')]//button")
        self.have_angry = (By.XPATH, "//li[contains(., 'Angry')]//button")
        self.remove_1_happy = (By.XPATH, "//a[@href='/reduce/5dd8e2b26c26d0000a675cf9' and text()='Remove 1']")
        self.remove_1_sad = (By.XPATH, "//a[@href='/reduce/5dd8e2b26c26d0000a675cfb' and text()='Remove 1']")
        self.remove_1_angry = (By.XPATH, "//a[@href='/reduce/5dd8e2b26c26d0000a675cfa' and text()='Remove 1']")
        self.remove_all_happy = (By.XPATH, "//a[@href='/remove/5dd8e2b26c26d0000a675cf9' and text()='Remove all']")
        self.remove_all_sad = (By.XPATH, "//a[@href='/remove/5dd8e2b26c26d0000a675cfb' and text()='Remove all']")
        self.remove_all_angry = (By.XPATH, "//a[@href='/remove/5dd8e2b26c26d0000a675cfa' and text()='Remove all']")
        self.empty_shopping_cart = (By.XPATH, "//h2[text()='Add items to the cart']")

    def verify_happy (self):
        self.find_elements(self.have_happy)

    def verify_sad(self):
        self.find_elements(self.have_sad)

    def verify_angry(self):
        self.find_element(self.have_angry)

    def verify_all_stickers(self):
        self.find_elements(self.have_happy)
        self.find_elements(self.have_sad)
        self.find_elements(self.have_angry)

    def click_go_to_cart_button(self):
        self.click(self.go_to_cart_button)

    def click_shopping_cart_button(self):
        self.click(self.shopping_cart_button)

    def click_on_sticker(self):
        self.click(self.have_happy)

    def remove_1_sticker(self):
        self.click(self.remove_1_happy)

    def click_on_and_remove_1_each_sticker(self):
        self.click(self.have_happy)
        self.click(self.remove_1_happy)
        time.sleep(1)
        self.click(self.have_sad)
        self.click(self.remove_1_sad)
        time.sleep(1)
        self.click(self.have_angry)
        self.click(self.remove_1_angry)
        time.sleep(1)

    def click_on_and_remove_all_each_sticker(self):
        self.click(self.have_happy)
        self.click(self.remove_all_happy)
        time.sleep(1)
        self.click(self.have_sad)
        self.click(self.remove_all_sad)
        time.sleep(1)
        self.click(self.have_angry)
        self.click(self.remove_all_angry)
        time.sleep(1)


    def empty_page(self):
        self.wait_element(self.empty_shopping_cart)

