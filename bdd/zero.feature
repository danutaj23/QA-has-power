Feature: Test of car dealer site

  Scenario: log in
    Given the page "http://salon.rpgit.pl/" is loaded
    When I type "danuta.klos" in "id_username" input
    When I type "Welcome1" in "id_password" input
    When I click "id_login_btn" button
    Then the home page is displayed

  Scenario Outline: add a new car
    When I click "add-new-car" button
    And I select "<brand>" from "id_marka" select
    And I type "<model>" in "id_model" input
    And I type "<year>" in "id_rocznik" input
    And I click Zapisz
    Then there is a car: brand "Audi", model "R8", year "2016"

    Examples:
      | brand   | model   | year |
      | Audi    | A1      | 2012 |
      | Audi    | Q3      | 2010 |
      | Hyundai | i40     | 2011 |
      | Hyundai | i30     | 2013 |
