import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.checkout_page = (By.XPATH, "//a[@href='/checkout' and text()='Checkout']")
        self.confirm_checkout_page = (By.XPATH, "//h4[text()='Thanks for your order!']")
        self.empty_chechout_page = (By.XPATH, "//h2[text()='Add items to the cart']")

    def full_checkout_page(self):
        self.find_element(self.checkout_page)
        self.click(self.checkout_page)
        self.wait_element(self.confirm_checkout_page)

    def empty_checkout_page(self):
        self.wait_element(self.empty_chechout_page)
