### General information
We are writing automation to simplify the work of the development team and manual testers.
Doing it in **Gherkin** syntax, using **Behave**.
Usually separate files are used for this purpose:
- `.feature` file, for writing test scripts in the Gherkin language. 
- `.py` file to define your step definitions.

.feature file structure standard:
```
Feature: 

Background:
    Given
    
@tag1 @tag2 @tag3
Scenario:
    Given
    When
    Then
  
@tag1 @tag2 @tag3
Scenario Outline:
    Given
    When
    Then
   
 Examples:
    | column1 | column2 | column3 |
    | value1  | value2  | value3  |
```


### 1. Feature
Is used to define the main functionality or capability that needs to be described and tested. Describe the overall goal or purpose of the feature to help better understand what will be tested in the corresponding scenarios in current feature file.
### 2. Tags
Tags are used to mark scenarios and allow classification based on specific categories or properties. Their usage can help in organizing and executing a test suite, filtering and grouping scenarios, as well as managing their execution.

Here are a few principles of using tags that we follow:

2.1 Classification by application (_**use the original name of the application for tagging it**_): `@Spotify`

2.2 Integration with test suites: `@acceptance_test`, `@regression_test`, `@load_test`, `@stress_test`, `@API_test`, `@compatibility_test`

2.3 Functional classification (**_write the tag with a small letter. If there are two words or more - use underscore to separate them_**): `@playlist`, `@payment`, `@login`

2.4 Classification by test author (_**pick one name and use it always**_): `@Witcher`, `@FreddieMercury`, `@potato`

### 3. Scenario name
`Scenario:` This is used to define a specific scenario or test case. 
There are no clear rules for formulating tests, but let's agree to maintain a some standard, according to which all tests can have the same name idea:

**what it tests - where it tests - under what conditions it tests**
- Avoid ambiguous or overly generic titles.
- Avoid overly long or confusing phrases.
- Specify the expectation of a successful or unsuccessful result
```
Scenario: Checking the successful cooking of an Explosion Muffin recipe with specific ingredients
```
### 4. Steps
#### 4. 1 Main syntax:
1. The `Given` keyword is used to describe the initial state or preconditions of the scenario. It sets up the necessary context for the test.
2. The `Background` keyword is used to define steps that are common to all scenarios within a feature file. It helps in reducing duplication of steps and sets up the initial state for scenarios. (Similar to `Given`, but more generally, within a single feature file.)
3. The `When` keyword is used to describe the action or event that is being performed in the scenario. It represents the user interaction or system behavior.
4. The `Then` keyword is used to describe the expected outcome or result of the scenario. It represents the expected behavior or verification point.

Note: At times, some use the `And` keyword, that used to combine multiple steps of the same type (Given, When, Then). It **NOT** helps improve readability and maintainability of the scenarios. It just confuses everyone. So, **don't use it.**

#### 4.2 Syntax features:
1. **Parameters**. Placeholders used in Scenario to represent dynamic values. They are defined within "<>" brackets and can be replaced with actual values during scenario execution.
```
#Example in test script

When I eat <eat> cucumbers
Then I should have <left> cucumbers
```
2. **Scenario Outline / Examples**. Used to provide a table of data with multiple sets of input values. This allows you to run the same script with different inputs.
```
#Example in test script

Scenario Outline: eating
  Given there are <start> cucumbers
  When I eat <eat> cucumbers
  Then I should have <left> cucumbers

  Examples:
    | start | eat | left |
    |    12 |   5 |    7 |
    |    20 |   5 |   15 |
```
3. **Data table parameter.** Used to pass tabular data as input to a step. It allows you to organize and pass structured data to steps in a scenario.
```
#Example in test script

When I have the following ingredients:
    | Ingredient  | Quantity |
    | Flour       | 200g     |
    | Sugar       | 150g     |
    | Eggs        | 3        |
    | Butter      | 100g     |
    | Vanilla     | 1 tsp    |
Then I can cook a Magic Pie
    
#Example in code
#For the steps that involve Data Tables, you can iterate over the table rows using context.table.

@when('I have the following ingredients:')
def when_ingredients(context):
    # Implement the when step to handle the data table
    for row in context.table:
        ingredient = row["Ingredient"]
        quantity = row["Quantity"]
        # Process each ingredient and quantity as needed
    pass
```

### 5. Test scenario
1. **Readability and clarity:** Scenarios should be easy to read and understand for all team members, including testers, developers, and business analysts. Use clear and simple language, avoid complex terms, and clarify the steps of the scenario to ensure they are clear and unambiguous.
Use the standard for naming elements:
- `Buttons` - testing interaction with buttons, including clicks and verifying the expected response.
- `Input Fields` - validating data input in text fields and checking for proper validation.
- `Dropdown Lists` - selecting or verifying options from drop-down lists.
- `Checkboxes/Radio Buttons` - verifying the selection of one or multiple options from checkboxes or radio buttons.
- `Links` - testing the functionality of links and verifying successful navigation to corresponding pages.
- `Tables` - testing interaction with data in tables, including sorting, filtering, and scrolling.
- `Tooltips` - testing the display and accuracy of tooltips.
- `Validation Messages` - verifying the display and correctness of validation messages for incorrect inputs.
- `Popup Windows` - verifying the opening, closing, and interaction with modal windows.
- `Status Messages` - testing the display and accuracy of status messages such as success, error, warning, etc.
- `Menu` - testing the opening and interaction with menus, including submenus and option selection.
- `Tabs` - testing tab switching and interaction with different interface tabs.
- `Panels` - verifying the visibility and interaction with different panels on a page.
- `Images` - testing the display and correctness of images, including checking for loading and resolution. 

2. **Atomicity**: Each scenario should test only one aspect or functionality of the system. This allows for easier understanding and isolation of issues when errors occur. Break down complex scenarios into smaller, atomic tests.
_**Try not to write tests longer than ~20 lines.**_
4. **Independence**: Scenarios should be independent of each other. Each scenario should be self-contained and not rely on the state or results of other scenarios. This enables more flexible and reliable execution of scenarios independently. **_If you need to handle entities, create them in the test. And don't forget to delete them after the test is executed._**
5. **Coverage of functionality**: Your scenarios should cover the main functional requirements and use different combinations of input data and actions to ensure sufficient coverage of the system's functionality. Pay attention to boundary conditions and potential errors.
6. **Maintainability**: Test scenarios should be easy to maintain and modify over time. Use parameterization and templates to simplify changes and reuse scenarios. Ensure clear organization and structure of scenarios, making it easy to add new ones and modify existing steps.
7. **Maintainability**: Scenarios should be easily updatable and adaptable to changes in the system or requirements. Add comments if needed and explanations where necessary to help future developers or testers understand the purpose and expectations of each step in the scenario.


### 6. Merging
1. Before creating a pull request, **make sure that your test passes successfully and does not break the build**.
2. Update your branch from master.
3. **Watch for line breaks!! ;)**
4. **Feature file capacity:** Max 5 tests in one feature file.
5. **Change size:** Try to make changes small and logically related so that they can be easily understood and reviewed. Large and complex changes can make the review process difficult and increase the likelihood of missing errors. 
6. **Change submission speed**: Aim to submit critical changes as quickly as possible. Critical changes are those that affect all team members and help them in their work processes. **It is better to create a separate branch for small and important tasks, where only one feature with refactoring will be included, to expedite the delivery of changes.**
