import pytest
from selenium import webdriver

driver: webdriver.Remote

@pytest.fixture()
def setup_teardown():

    #setup (you must define global driver)
    global driver
    driver = webdriver.Edge()
    driver.get('https://stickerfy.herokuapp.com/')
    driver.maximize_window()

    #call tests and run
    yield

    #tear_down
    driver.quit()