Feature: Login

  Scenario Outline: Login behavior for valid, invalid and locked-out users
    Given I open the login page
    When I login as "<user_key>"
    Then I should see "<expected_result>"

    Examples:
      | user_key         | expected_result |
      | valid_user       | success         |
      | invalid_user     | invalid_error   |
      | locked_out_user  | locked_out_error|

