import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self): #construtor da classe
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//a[@class='navbar-brand' and text()='Stickerfy']")

    def successful_login(self):
        self.navbar_title(self.page_title)