Feature: AppiumDemo - Login

  Background:
    Given Relaunching App

    # here should be tags for scenario
  Scenario: Login
    When User goes to Login page
    When User put email admin@gmail.com and password admin123