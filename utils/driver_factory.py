from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config import HEADLESS

def create_driver():
    options = Options()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }

    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--incognito")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    return driver