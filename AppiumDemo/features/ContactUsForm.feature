Feature: AppiumDemo - ContactUsForm

  Background:
    Given Relaunching App

    # here should be tags for scenario
  Scenario Outline: Fill the contact us form
    When User goes to ContactUsForm page
    When User fill the form with name: <name>, email: <email>, address: <address>, mobile: <mobile>
    Then User checks if output is same as input
    Examples:
    |name    |email                  |address   |mobile   |
    |Krystian|krystian.kiel@gmail.com|Polska    |666777999|
    |Jan     |kowalski@email.com     |Uzbekistan|111222333|

