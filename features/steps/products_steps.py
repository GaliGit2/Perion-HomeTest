from behave import  then, given


@then("I should see a non-empty product list")
def step_non_empty_list(context):
    names = context.products_page.get_product_names()
    assert len(names) > 0, "Expected at least 1 product"

@then("all product names should be non-empty")
def step_names_not_empty(context):
    names = context.products_page.get_product_names()
    assert all(n != "" for n in names), f"Found empty product name in: {names}"

@then("all product prices should be greater than 0")
def step_prices_gt_zero(context):
    prices = context.products_page.get_product_prices()
    assert all(p > 0 for p in prices), f"Found non-positive price in: {prices}"

@given('I sort products by "{sort_mode}"')
def step_sort(context, sort_mode):
    context.products_page.sort_by_visible_text(sort_mode)

@then('product prices should be sorted "{expected_order}"')
def step_verify_sort(context, expected_order):
    prices = context.products_page.get_product_prices()
    sorted_prices = sorted(prices)
    if expected_order == "ascending":
        assert prices == sorted_prices, f"Prices not ascending. Got: {prices}"
    elif expected_order == "descending":
        assert prices == list(reversed(sorted_prices)), f"Prices not descending. Got: {prices}"
    else:
        assert False, f"Unknown expected_order: {expected_order}"