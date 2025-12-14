from behave import when, then
from utils.config import ROUND_DECIMALS_POINT, EMPTY_CART_ITEMS_COUNT, CHECKOUT_CSV_PATH, EMPTY_CART_Total
from utils.data_loader import load_checkout_data
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage

@when("I start checkout")
def step_start_checkout(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.click_checkout()
    context.checkout_one = CheckoutStepOnePage(context.driver)
    context.checkout_one.wait_loaded()

@when('I enter checkout details from CSV row "{row_index}"')
def step_enter_details(context, row_index):
    data = load_checkout_data(CHECKOUT_CSV_PATH)
    info_index = int(row_index)
    if info_index < 0 or info_index >= len(data):
        raise AssertionError(f"CSV row_index out of range: {info_index}. Rows={len(data)}")
    info = data[info_index]
    context.checkout_one.fill_and_continue(
        first_name=info["first_name"],
        last_name=info["last_name"],
        postal_code=info["postal_code"],
    )
    context.checkout_two = CheckoutStepTwoPage(context.driver)
    context.checkout_two.wait_loaded()


@then("the order summary should match items sum plus tax")
def step_verify_totals(context):
    prices = context.checkout_two.get_item_prices()
    item_total = context.checkout_two.get_item_total()
    tax = context.checkout_two.get_tax()
    total = context.checkout_two.get_total()
    calc_sum = round(sum(prices), ROUND_DECIMALS_POINT)
    assert round(item_total, ROUND_DECIMALS_POINT) == calc_sum, (
        f"Item total mismatch. UI={item_total} Calc={calc_sum} Prices={prices}"
    )
    calc_total = round(item_total + tax, ROUND_DECIMALS_POINT)
    assert round(total, ROUND_DECIMALS_POINT) == calc_total, (
        f"Total mismatch. UI={total} Calc={calc_total} "
        f"(item_total={item_total}, tax={tax})"
    )
    context.checkout_two.finish()

@then("I should see a successful order completion message")
def step_success_message(context):
    complete_page = CheckoutCompletePage(context.driver)
    msg = complete_page.get_success_message()
    assert "thank you" in msg.lower(), f"Unexpected success message: {msg}"

@then("the checkout summary should show 0 items")
def step_checkout_zero_items(context):
    items_count = context.checkout_two.get_items_count()
    assert items_count == EMPTY_CART_ITEMS_COUNT, (
        f"Expected {EMPTY_CART_ITEMS_COUNT} items in checkout summary, got {items_count}"
    )

@then("the item total should be 0.00")
def step_item_total_zero(context):
    total = round(context.checkout_two.get_item_total(), ROUND_DECIMALS_POINT)
    assert total == EMPTY_CART_Total, f"Expected item total {EMPTY_CART_Total}, got {total}"