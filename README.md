# Selenium Project - Page Object Model (POM)

This project uses the Page Object Model (POM) pattern for automated tests with Selenium. 
It was developed to test the [Stickerfy](https://stickerfy.herokuapp.com/) website and organizes test scenarios for different interactions on the site.
Based in pytest framework tool, using fixtures to invoke conftest.py and with specific names for each test.

## Project Structure

```
selenium-project-pom/
|-- .venv/                              # Virtual environment containing dependencies
|-- conftest.py                         # Global configurations and pytest fixtures
|-- pages/                              # POM files representing the site pages
|   |-- __init__.py                     # Makes the folder a Python module
|   |-- base_page.py                    # Base class with reusable generic methods
|   |-- checkout_page.py                # Represents the checkout page
|   |-- home_page.py                    # Represents the homepage
|   |-- select_sticker.py               # Manages sticker selection
|   |-- shopping_cart_page.py           # Manages interactions on the shopping cart page
|
|-- tests/                              # Tests organized by scenario
    |-- firstScenario                   # Tests using "Go to Cart" button
    |-- secondScenario                  # Tests using "Shopping Cart" button
    |-- thirdScenario                   # Tests for remove one of each stickers
    |-- foutyScenario                   # Tests for remove all sctickers

## Prerequisites

1. Python 3.8 or higher installed.
2. Google Chrome installed.
3. ChromeDriver compatible with your Chrome version.
4. Install project dependencies:

```bash
pip install selenium pytest
```

## Project Pattern (POM)

The Page Object Model pattern organizes code so that interaction logic with the interface is separate from the tests. This facilitates maintenance and reuse.

- **`base_page.py`**:
  Contains reusable generic methods, such as clicking on elements or locating them.

- **Other files in `pages/`**:
  Each file represents a page of the site, encapsulating specific elements and their interactions.

Example of a method in `base_page.py`:

```python
import conftest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def find_element(self, locator):
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
```

## Running the Tests

1. Clone the repository:

```bash
git clone https://github.com/alisson-t-bucchi/stickerfy_selenium_python.git 
```

2. Navigate to the project directory:

```bash
cd stickerfy-selenium-python
```

3. Run the all tests:

```bash
pytest tests
```

4. Run one specific test:

```bash
pytest .\tests\(path to the test)
```

5. Run the all tests with HTML Report and customize the report location (here called reports folder), filename and an the report title:

```bash
pytest tests/ --html-report=./reports/ --title='write you report name here!'
```
The results will be displayed into the reports folder with 2 files:
1. output.json
2. pytest_html_report.html (open with your favourite browser to see the results)

## Test Structure

Tests are organized by scenario within the `tests/` folder. Each subfolder represents a specific flow based in diferent buttons or functions presented in each screen:

1. **`using_go_to_cart_button/`**:
   Tests navigation to the cart using the "Go to Cart" button.

2. **`using_remove_1_button/`**:
   Validates the removal of items from the cart.

3. **`using_shopping_cart_button/`**:
   Tests navigation to the cart using the "Shopping Cart" button.

Example of a test:

```python
import pytest
import conftest
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.select_sticker import SelectSticker
from pages.shopping_cart_page import ShoppingCartPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.buyHappyScene1

class TestBuyHappy:
    def test_buy_happy(self):
        driver = conftest.driver
        home_page = HomePage()
        select_sticker = SelectSticker()
        go_to_cart_page = ShoppingCartPage()
        verify_products = ShoppingCartPage()
        complete_checkout = CheckoutPage()

        #open Stickerfy page.
        home_page.successful_login()

        #select Happy sticker clicking in Add to cart blue button.
        select_sticker.sticker_happy()

        #go to cart page.
        go_to_cart_page.click_go_to_cart_button()

        #verification of Happy Sticker into cart page.
        verify_products.verify_happy()

        #click on checkout and confirm checkout.
        complete_checkout.full_checkout_page()
```

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements.

## License

This project is licensed under the MIT License.