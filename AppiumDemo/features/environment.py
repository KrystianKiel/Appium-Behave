# -*- coding: utf-8 -*-

"""Module contains all preconditions, postconditions and all data needed to
prepare driver."""

from appium import webdriver
# from appium.options.ios import XCUITestOptions
from appium.options.android import UiAutomator2Options
import allure


def before_all(context):
    """Creating driver with capabilities"""

    """New capabilities on Appium-Python-Client 3.0.0"""
    capabilities = UiAutomator2Options().load_capabilities({
        'platformName': 'Android',
        'automationName': 'uiautomator2',
        'deviceName': 'emulator-5554',
        'appPackage': 'com.skill2lead.appiumdemo',
        'appActivity': 'com.skill2lead.appiumdemo.MainActivity'
    })
    context.driver = webdriver.Remote('http://127.0.0.1:4723',
                                      options=capabilities,
                                      direct_connection=True)

    """For older version Appium-Python-Client 2.3.0"""
    # capabilities = { 'platformName': 'Android', 'automationName':
    # 'uiautomator2', 'deviceName': 'emulator-5554', 'appPackage':
    # 'com.skill2lead.appiumdemo', 'appActivity':
    # 'com.skill2lead.appiumdemo.MainActivity' } server_urls = [
    # 'http://192.168.0.24:4723/', 'http://127.0.0.1:4723/',
    # 'http://127.0.0.1:4723/wd/hub', 'http://0.0.0.0:4723']

    # for server_url in server_urls:
    #     try:
    #
    #         context.driver = webdriver.Remote(server_url, capabilities)
    #         print(f"Connect with: {server_url}")
    #         sleep(2)
    #         break
    #     except Exception as e:
    #         print(f"Cannot connect with: {server_url}")
    #         print(f"Error: {str(e)}")
    #         sleep(2)
    #         continue


def after_step(context, step):
    if step.status == "failed":
        """Catch screenshot on failed step"""
        driver = context.driver
        allure.attach(driver.get_screenshot_as_png(), name=None,
                      attachment_type=allure.attachment_type.PNG)
        """Catch logs on failed step"""
        logs = driver.get_log("logcat")
        log_text = "\n".join([log["message"] for log in logs])
        allure.attach(log_text, name="App Logs",
                      attachment_type=allure.attachment_type.TEXT)


def after_all(context):
    """Disconnect driver"""
    print("Driver disconnect")
    context.driver.quit()
