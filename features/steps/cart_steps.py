from behave import when, then
from pages.products_page import ProductsPage
from utils.config import INITIAL_CART_ITEMS_COUNT, CART_ITEMS_COUNT


@when("I add 3 products to the cart")
def step_add_three(context):
    context.added_products = context.products_page.get_first_n_product_names(INITIAL_CART_ITEMS_COUNT)
    for name in context.added_products:
        context.products_page.add_product_by_name(name)
    context.product_to_remove = context.added_products[1]

@then("the cart badge should show 3")
def step_badge_3(context):
    assert context.products_page.get_cart_badge_count() == INITIAL_CART_ITEMS_COUNT

@when("I remove 1 product from the cart")
def step_remove_one(context):
    context.cart_page.remove_item_by_name(context.product_to_remove)

@then("the cart badge should show 2")
def step_badge_2(context):
    assert ProductsPage(context.driver).get_cart_badge_count() == CART_ITEMS_COUNT