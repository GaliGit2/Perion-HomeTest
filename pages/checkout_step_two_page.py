from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import CHECKOUT_STEP_TWO


class CheckoutStepTwoPage(BasePage):
    ITEM_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    ITEM_TOTAL = (By.CSS_SELECTOR, ".summary_subtotal_label")
    TAX = (By.CSS_SELECTOR, ".summary_tax_label")
    TOTAL = (By.CSS_SELECTOR, ".summary_total_label")
    FINISH_BTN = (By.ID, "finish")

    def wait_loaded(self):
        self.wait_url_contains(CHECKOUT_STEP_TWO)
        self.wait_visible(self.FINISH_BTN)

    def get_item_prices(self):
        self.wait_loaded()
        prices = []
        for item_price in self.find_all(self.ITEM_PRICES):
            txt = item_price.text.strip().replace("$", "")
            prices.append(float(txt))
        return prices

    def _money_from_label(self, label_text: str) -> float:
        return float(label_text.split("$")[-1].strip())

    def get_item_total(self) -> float:
        return self._money_from_label(self.text_of(self.ITEM_TOTAL))

    def get_tax(self) -> float:
        return self._money_from_label(self.text_of(self.TAX))

    def get_total(self) -> float:
        return self._money_from_label(self.text_of(self.TOTAL))

    def finish(self):
        self.click(self.FINISH_BTN)

    def get_items_count(self) -> int:
        self.wait_loaded()
        return len(self.find_all(self.ITEM_PRICES))