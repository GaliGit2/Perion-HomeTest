import os

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")
BROWSER = os.getenv("BROWSER", "chrome")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

CART_PATH = "cart.html"
INVENTORY_PAGE = "inventory"
ROUND_DECIMALS_POINT = 2
EMPTY_CART_ITEMS_COUNT = 0
EMPTY_CART_TOTAL = 0.00
CHECKOUT_STEP_ONE = os.getenv("CHECKOUT_STEP_ONE","checkout-step-one")
CHECKOUT_STEP_TWO = os.getenv("CHECKOUT_STEP_TWO","checkout-step-two")
CHECKOUT_COMPLETE = os.getenv("CHECKOUT_COMPLETE","checkout-complete")
INITIAL_CART_ITEMS_COUNT = os.getenv("INITIAL_CART_ITEMS_COUNT", 3)
CART_ITEMS_COUNT =  os.getenv("INITIAL_CART_ITEMS_COUNT", 2)

USERS_PATH = os.getenv("USERS_PATH", "data/users.json")
SCREENSHOTS_DIR = os.getenv("SCREENSHOTS_DIR", "screenshots")
CHECKOUT_CSV_PATH = os.getenv("CHECKOUT_CSV_PATH", "data/checkout_data.csv")
TIMEOUT = int(os.getenv("TIMEOUT", "10"))