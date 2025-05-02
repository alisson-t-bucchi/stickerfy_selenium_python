import conftest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def find_element(self, locator):
        # o uso do * serve para iterar os elementos presentes em uma variavel.
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        return self.find_element(locator).click()

    def navbar_title(self, locator):
        assert self.find_element(locator).is_displayed(), f"Element {'locator'} not found!"

    def find_text_element(self, locator):
        self.wait_element(locator)
        return self.find_text_element(locator).text

    def wait_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def double_click(self, locator):
        element = self.find_element(locator)
        ActionChains(self.driver).double_click(element).perform()

