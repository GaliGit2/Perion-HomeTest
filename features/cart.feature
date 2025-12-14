Feature: Cart

  Scenario: Add products to cart, verify badge, remove one product
    Given I login successfully
    And I am on the products page
    When I add 3 products to the cart
    Then the cart badge should show 3
    When I open the cart
    Then the cart should contain 3 items
    When I remove 1 product from the cart
    Then the cart badge should show 2
    And the cart should contain 2 items