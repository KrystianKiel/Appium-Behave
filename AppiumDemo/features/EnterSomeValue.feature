Feature: AppiumDemo - EnterSomeValue

  Background:
    Given Relaunching App

    # here should be tags for scenario
  Scenario: Enter some value to text box
    When User goes to EnterSomeValue page
    When User inputs value: Some Value
    Then User checks if output is same as input