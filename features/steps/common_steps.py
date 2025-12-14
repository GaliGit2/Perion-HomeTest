from behave import given, when, then
from pages.cart_page import CartPage
from pages.products_page import ProductsPage
from utils.auth import login_as
from utils.config import INVENTORY_PAGE

@given("I login successfully")
def step_login_success(context):
    login_as(context.driver, "valid_user")

@given("I am on the products page")
def step_on_products(context):
    assert INVENTORY_PAGE in context.driver.current_url, (
        f"Not on {INVENTORY_PAGE} page. URL={context.driver.current_url}"
    )
    context.products_page = ProductsPage(context.driver)
    context.products_page.wait_loaded()

@when("I open the cart")
def step_open_cart(context):
    context.products_page.open_cart()
    context.cart_page = CartPage(context.driver)
    context.cart_page.wait_loaded()

@then('the cart should contain {expected_count:d} items')
def step_cart_should_contain_n_items(context, expected_count):
    cart = CartPage(context.driver)
    cart.wait_loaded()
    actual = cart.get_items_count()
    assert actual == expected_count, f"Expected {expected_count} items in cart, got {actual}"
