from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from utils.config import CART_PATH


class ProductsPage(BasePage):
    INVENTORY_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")
    SORT_SELECT = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    ITEM_NAME_IN_ITEM = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_BUTTON_IN_ITEM = (By.CSS_SELECTOR, "button.btn_inventory")

    def wait_loaded(self):
        self.wait_visible(self.INVENTORY_ITEMS)

    def get_product_names(self):
        self.wait_loaded()
        return [e.text.strip() for e in self.find_all(self.ITEM_NAME)]

    def get_product_prices(self):
        self.wait_loaded()
        prices = []
        for item_price in self.find_all(self.ITEM_PRICE):
            txt = item_price.text.strip().replace("$", "")
            prices.append(float(txt))
        return prices

    def sort_by_visible_text(self, text: str):
        self.wait_loaded()
        self.wait_visible(self.SORT_SELECT)
        self.wait_clickable(self.SORT_SELECT)
        select_el = self.find(self.SORT_SELECT)
        Select(select_el).select_by_visible_text(text)

    def get_first_n_product_names(self, n: int = 3):
        self.wait_loaded()
        items = self.find_all(self.INVENTORY_ITEMS)
        names = []
        for item in items[:n]:
            name = item.find_element(*self.ITEM_NAME_IN_ITEM).text.strip()
            if not name:
                raise AssertionError("Found empty product name while selecting first N products")
            names.append(name)
        if len(names) < n:
            raise AssertionError(f"Expected at least {n} products, found {len(names)}")
        return names

    def add_product_by_name(self, product_name: str):
        self.wait_loaded()
        items = self.find_all(self.INVENTORY_ITEMS)
        for item in items:
            name_el = item.find_element(*self.ITEM_NAME_IN_ITEM)
            if name_el.text.strip() == product_name:
                item.find_element(*self.ITEM_BUTTON_IN_ITEM).click()
                return
        raise AssertionError(f"Product not found on page: {product_name}")

    def get_cart_badge_count(self) -> int:
        badges = self.driver.find_elements(*self.CART_BADGE)
        if not badges:
            return 0
        txt = badges[0].text.strip()
        return int(txt) if txt else 0

    def open_cart(self):
        self.click(self.CART_LINK)
        self.wait_url_contains(CART_PATH)
