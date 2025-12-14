from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import BASE_URL, TIMEOUT

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver, timeout=TIMEOUT)

    def open(self, url: str = BASE_URL):
        self.driver.get(url)
        self.wait_visible(self.USERNAME)

    def login(self, username: str, password: str):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def error_message(self) -> str:
        return self.text_of(self.ERROR)