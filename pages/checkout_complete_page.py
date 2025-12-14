from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import CHECKOUT_COMPLETE


class CheckoutCompletePage(BasePage):
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")

    def wait_loaded(self):
        self.wait_url_contains(CHECKOUT_COMPLETE)
        self.wait_visible(self.COMPLETE_HEADER)

    def get_success_message(self) -> str:
        self.wait_loaded()
        return self.text_of(self.COMPLETE_HEADER)