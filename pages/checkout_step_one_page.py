from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import CHECKOUT_STEP_ONE


class CheckoutStepOnePage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")

    def wait_loaded(self):
        self.wait_url_contains(CHECKOUT_STEP_ONE)
        self.wait_visible(self.FIRST_NAME)

    def fill_and_continue(self, first_name: str, last_name: str, postal_code: str):
        self.wait_loaded()
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BTN)