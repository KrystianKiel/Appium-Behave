import time
from behave import given, when, then
from AppiumDemo.pages.basepage import BasePage
from AppiumDemo.pages.entersomevalue import EnterSomeValue
from AppiumDemo.pages.contactusform import ContactUsForm
from AppiumDemo.pages.scrollview import ScrollView
from AppiumDemo.pages.tabactivity import TabActivity
from AppiumDemo.pages.login import LoginPage


@given('Relaunching App')
def reset_driver(context):
    BasePage.terminate_app(context, 'com.skill2lead.appiumdemo')
    BasePage.activate_app(context, 'com.skill2lead.appiumdemo')
    time.sleep(2)


@when('User goes to {page} page')
def go_to_page(context, page):
    if page == 'EnterSomeValue':
        EnterSomeValue.go_to_entersomevalue(context)
    elif page == 'ContactUsForm':
        ContactUsForm.go_to_contactusform(context)
    elif page == 'ScrollView':
        ScrollView.go_to_scrollview(context)
    elif page == 'TabActivity':
        TabActivity.go_to_tabactivity(context)
    elif page == 'Login':
        LoginPage.go_to_login(context)


@when('User inputs value: {value}')
def inputs_value(context, value):
    current_scenario_name = context.scenario.name
    if 'entersomevalue' in current_scenario_name.replace(" ", "").lower():
        EnterSomeValue.put_value(context, value)


@when('User fill the form with name: {value}, email: {value2}, address: {'
      'value3}, mobile: {value4}')
def fill_the_form(context, value, value2, value3, value4):
    ContactUsForm.put_value(context, value, value2, value3, value4)


@then('User checks if output is same as input')
def check_output(context):
    current_feature_name = context.feature.name
    if 'entersomevalue' in current_feature_name.replace(" ", "").lower():
        value = BasePage.text(context, EnterSomeValue.text_box)
        EnterSomeValue.check_if_value_valid(context, value)
    elif 'contactusform' in current_feature_name.replace(" ", "").lower():
        ContactUsForm.check_if_value_valid(context)


@when('User scroll down to {button_number} button and click')
def scroll_down_to_button(context, button_number):
    BasePage.is_element_visible_by_swipe_down(
        context, f"//*[@text='BUTTON{button_number}']")
    BasePage.click_element(context, f"//*[@text='BUTTON{button_number}']")


@then('User confirm popup alert and check if return to home page')
def return_and_check(context):
    BasePage.is_element_visible_by_swipe_down(context, ScrollView.Alert)
    BasePage.click_element(context, ScrollView.Yes_button)
    BasePage.is_element_visible_by_swipe_down(context,
                                              EnterSomeValue.enter_some_value)


@when('User swiping to the {page} page')
def swiping_to_the_page(context, page):
    if page == 'Movie':
        TabActivity.swipe_to_movie(context)
    elif page == 'Home':
        TabActivity.swipe_to_home(context)


@when ('User put email {email} and password {password}')
def put_credential(context, email, password):
    LoginPage.put_credential(context, email, password)
