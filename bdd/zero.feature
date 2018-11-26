Feature: Test of car dealer site

  Scenario: log in
    Given the page "http://salon.rpgit.pl/" is loaded
    When I type "danuta.klos" in "id_username" input
    When I type "Welcome1" in "id_password" input
    When I click "id_login_btn" button
    Then the home page is displayed
