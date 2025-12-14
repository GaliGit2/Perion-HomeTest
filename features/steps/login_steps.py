from behave import given, when, then
from pages.login_page import LoginPage
from utils.config import BASE_URL, INVENTORY_PAGE
from utils.auth import login_as

ERROR_EXPECTATIONS = {
    "invalid_error": "do not match any user",
    "locked_out_error": "locked out",
}

@given("I open the login page")
def step_open_login(context):
    context.page = LoginPage(context.driver)
    context.page.open(BASE_URL)

@when('I login as "{user_key}"')
def step_login(context, user_key):
    login_as(context.driver, user_key)


@then('I should see "{expected_result}"')
def step_verify(context, expected_result):
    if expected_result == "success":
        assert INVENTORY_PAGE in context.driver.current_url
        return
    expected_substring = ERROR_EXPECTATIONS.get(expected_result)
    assert expected_substring, f"Unknown expected_result: {expected_result}"
    actual = context.page.error_message().lower()
    assert expected_substring in actual, f"Expected '{expected_substring}' in '{actual}'"