from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_url_contains(self, text: str):
        return self.wait.until(EC.url_contains(text))


    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)


    def click(self, locator):
        self.wait_clickable(locator).click()

    def type(self, locator, text: str, clear=True):
        textbox = self.wait_visible(locator)
        if clear:
            textbox.clear()
        textbox.send_keys(text)

    def text_of(self, locator) -> str:
        return self.wait_visible(locator).text.strip()