from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import CART_PATH


class CartPage(BasePage):
    CART_ITEM = (By.CSS_SELECTOR, ".cart_item")
    CART_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button.cart_button")
    CHECKOUT_BTN = (By.ID, "checkout")

    def wait_loaded(self):
        self.wait_url_contains(CART_PATH)

    def get_cart_item_names(self):
        self.wait_loaded()
        items = self.find_all(self.CART_ITEM)
        names = []
        for it in items:
            names.append(it.find_element(*self.CART_ITEM_NAME).text.strip())
        return names

    def remove_item_by_name(self, product_name: str):
        self.wait_loaded()
        items = self.find_all(self.CART_ITEM)
        for it in items:
            name = it.find_element(*self.CART_ITEM_NAME).text.strip()
            if name == product_name:
                it.find_element(*self.REMOVE_BUTTON).click()
                return
        raise AssertionError(f"Item not found in cart: {product_name}")

    def get_items_count(self) -> int:
        return len(self.find_all(self.CART_ITEM))

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)