from pages.login_page import LoginPage
from utils.config import BASE_URL
from utils.data_loader import load_users

def login_as(driver, user_key: str):
    users = load_users()
    creds = users[user_key]

    page = LoginPage(driver)
    page.open(BASE_URL)
    page.login(creds["username"], creds["password"])
    return page