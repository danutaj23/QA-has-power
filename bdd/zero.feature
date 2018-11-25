Feature: Test of car dealer site
  Scenario: log in
    Given the page is loaded
    When I fill username
    When I fill password
    When I click Zaloguj
    Then the home page is displayed
