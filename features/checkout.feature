Feature: Checkout

  Scenario Outline: Complete checkout with CSV data and verify totals
    Given I login successfully
    And I am on the products page
    When I add 3 products to the cart
    And I open the cart
    And I start checkout
    And I enter checkout details from CSV row "<row_index>"
    Then the order summary should match items sum plus tax
    And I should see a successful order completion message

    Examples:
      | row_index |
      | 0         |
      | 1         |

  Scenario: Empty cart checkout shows no items in summary
    Given I login successfully
    And I am on the products page
    When I open the cart
    Then the cart should contain 0 items
    When I start checkout
    And I enter checkout details from CSV row "0"
    Then the checkout summary should show 0 items
    And the item total should be 0.00