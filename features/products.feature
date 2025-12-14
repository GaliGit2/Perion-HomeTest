Feature: Products

  Background:
    Given I login successfully

  Scenario: Product listing is displayed with valid names and prices
    Given I am on the products page
    Then I should see a non-empty product list
    And all product names should be non-empty
    And all product prices should be greater than 0

  Scenario Outline: Sorting by price works
    Given I am on the products page
    And I sort products by "<sort_mode>"
    Then product prices should be sorted "<expected_order>"

    Examples:
      | sort_mode | expected_order |
      | Price (low to high)      | ascending      |
      | Price (high to low)      | descending     |