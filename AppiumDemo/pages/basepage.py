from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import re
import pkgutil
import AppiumDemo.pages as y


class BasePage:
    submit = "//*[@text='SUBMIT']"

    """Class contains all needed to test methods,

    :param WAIT_TIME: int - WebDriverWait timeout parameter measure in seconds.
    """
    wait_time = 1

    @staticmethod
    def find_button_by_text(name_text):
        xpath_selector = f"//*[@class='android.widget.TextView']" \
                         f"[@text='{name_text}']"
        return xpath_selector

    @staticmethod
    def where_is(xpath):
        """Method searching for location of requested xpath and return name
        of class where xpath is stored.

        :param xpath: str name of searched xpath.
        :return: str name of class which store xpath.
        """
        page_list = []
        chosen_file = []
        current_dir = os.getcwd()
        for i in list(pkgutil.iter_modules(y.__path__)):
            page_list.append(i.name)
        for file_name in page_list:
            with open(f"{current_dir}\AppiumDemo\pages\{file_name}.py",
                      "r") as f:
                file_access = f.readlines()
                for line in file_access:
                    line = line.rstrip()
                    if re.search(r"\b{}\b =".format(xpath), line):
                        chosen_file.append(file_name)
        if len(chosen_file) > 1:
            print("There are two variables with the same name")
        else:
            return chosen_file[0].capitalize()

    def click_element(self, element):
        """Click on chosen element.

        :param element: str - locator from xpath list.
        :return trigger click element.
        """
        try:
            click_element = WebDriverWait(self.driver,
                                          timeout=BasePage.wait_time,
                                          poll_frequency=0.1).until(
                lambda x: x.find_element(by=AppiumBy.XPATH, value=element))
            click_element.click()
        except TimeoutError:
            print("Cant find element")
            return False

    def is_element_visible(self, element: str):
        """Check if chosen element is visible.

        :param element: str - locator from xpath list.
        :rtype: True if method successful, otherwise False.
        :return: bool.
        """
        try:
            element_visible = WebDriverWait(self.driver,
                                            timeout=BasePage.wait_time,
                                            poll_frequency=0.1).until(
                lambda x: x.find_element(by=AppiumBy.XPATH, value=element))
            return element_visible.is_displayed()
        except Exception as e:
            print("Cant find element")
            print(f"Error: {str(e)}")
            return False

    def swipe_up(self):
        """Swipe up on the current screen.

        :rtype: evoke swiping up, when fail return False
        """
        size = self.driver.get_window_size()
        start_x = size['width'] // 2
        start_y = size['height'] // 4
        end = size['height'] // 2
        try:
            swipe_up = WebDriverWait(self.driver,
                                     timeout=BasePage.wait_time).until(
                lambda x: x.swipe(start_x, start_y, start_x, end))
            return swipe_up
        except TimeoutError:
            print("Cant swipe in requested time")
            return False

    def swipe_down(self):
        """Swipe down on the current screen.

        :rtype: evoke swiping down, when fail return False.
        """
        size = self.driver.get_window_size()
        start_x = size['width'] * 0.9
        start_y = size['height'] * 0.4
        end = size['height'] * 0.25
        try:
            swipe_up = WebDriverWait(self.driver,
                                     timeout=BasePage.wait_time).until(
                lambda x: x.swipe(start_x, start_y, start_x, end))
            return swipe_up
        except TimeoutError:
            print("Cant swipe in requested time")
            return False

    def send_key(self, element: str, value: str):
        """Send key on enter field.

        :param element: str - locator from xpath list.
        :param value: str - string which will be put.
        :rtype: evoke method send_kay which value, when fail return False.
        """
        try:
            send_key = WebDriverWait(self.driver,
                                     timeout=BasePage.wait_time).until(
                lambda x: x.find_element(by=AppiumBy.XPATH, value=element))
            return send_key.send_keys(value)
        except TimeoutError:
            print("Cant swipe in requested time")
            return False

    def text(self, element: str):
        """Find Text.

        :param element: str - locator from xpath list.
        :rtype: evoke method text, when fail return False.
        """
        try:
            find_text = WebDriverWait(self.driver,
                                      timeout=BasePage.wait_time).until(
                lambda x: x.find_element(by=AppiumBy.XPATH, value=element))
            return find_text.text
        except TimeoutError:
            print("Cant find element in requested time")
            return False

    # def reset(self):
    #     """NOT WORKING ON 3.0.0"""
    #     """Reset driver and back to main app package.
    #
    # :rtype: evoke method reset, when fail return False. """ try:
    # reset_driver = WebDriverWait(self.driver,
    # timeout=BasePage.WAIT_TIME).until(( lambda x: x.reset())) return
    # reset_driver except TimeoutError: print("Cant reset in requested
    # time") return False
    def terminate_app(self, app):
        """WORKING ON 3.0.0"""
        try:
            terminate = WebDriverWait(self.driver,
                                      timeout=BasePage.wait_time) \
                .until((lambda x: x.terminate_app(app)))
            return terminate
        except TimeoutError:
            print("Cant terminate in requested time")
            return False

    def activate_app(self, app):
        """WORKING ON 3.0.0"""
        try:
            activate = WebDriverWait(self.driver,
                                     timeout=BasePage.wait_time)\
                .until((lambda x: x.activate_app(app)))
            return activate
        except TimeoutError:
            print("Cant terminate in requested time")
            return False

    def swipe_left(self):
        """Swipe left on the current screen.

        :rtype: evoke swiping left, when fail return False.
        """
        size = self.driver.get_window_size()
        start_x = size['width'] * 0.2
        start_y = size['height'] // 2
        end = size['width'] * 0.8
        try:
            swipe_left = WebDriverWait(self.driver,
                                       timeout=BasePage.wait_time).until(
                lambda x: x.swipe(start_x, start_y, end, start_y))
            return swipe_left
        except TimeoutError:
            print("Cant swipe in requested time")
            return False

    def swipe_right(self):
        """Swipe right on the current screen.

        :rtype: evoke swiping right, when fail return False.
        """

        size = self.driver.get_window_size()
        start_x = size['width'] * 0.8
        start_y = size['height'] // 2
        end = size['width'] * 0.2
        try:
            swipe_right = WebDriverWait(self.driver,
                                        timeout=BasePage.wait_time).until(
                lambda x: x.swipe(start_x, start_y, end, start_y))
            return swipe_right
        except TimeoutError:
            print("Cant swipe in requested time")
            return False

    def long_click_1sec(self, element):
        """Long click on element.

        :param element: str - locator from xpath list. :return: trigger long
        click element while 1 second, when fail return False.
        """
        try:
            long_click = WebDriverWait(self.driver,
                                       timeout=BasePage.wait_time).until(
                (lambda x: x.find_element(by=AppiumBy.XPATH, value=element)))
            return TouchAction(self.driver).long_press(long_click,
                                                       duration=1000).perform()
        except TimeoutError:
            print("Cant find element in requested time")
            return False

    def long_click(self, element, duration: int):
        """Long click on element.

        :param element: str - locator from xpath list.
        :param duration: int - duration in seconds.
        :return: trigger long click element, when fail return False.
        """
        try:
            long_click = WebDriverWait(self.driver,
                                       timeout=BasePage.wait_time).until(
                (lambda x: x.find_element(by=AppiumBy.XPATH, value=element)))
            return TouchAction(self.driver).long_press(
                long_click, duration=duration).perform()
        except TimeoutError:
            print("Cant find element in requested time")
            return False

    def drag_and_drop_on_target(self, element, target):
        """Drag element and drop on target.

        :param element: str - locator from xpath list.
        :param target: str - locator from xpath list.
        :return: trigger long click element, when fail return False.
        """
        chosen_element = WebDriverWait(self.driver,
                                       timeout=BasePage.wait_time).until(
            (lambda x: x.find_element(by=AppiumBy.XPATH, value=element)))
        chosen_target = WebDriverWait(self.driver,
                                      timeout=BasePage.wait_time).until(
            (lambda x: x.find_element(by=AppiumBy.XPATH, value=target)))

        try:
            TouchAction(self.driver).press(chosen_element).move_to(
                chosen_target).release().perform()
        except TimeoutError:
            print("Cant move element in requested time")
            return False

    def is_element_visible_by_swipe_down(self, element: str):
        """Check if chosen element is visible.

        :param element: str - locator from xpath list. :return: find element
        by xpath, when fail swipe down and search further.
        """
        max_attempts = 5
        current_attempt = 1
        while current_attempt <= max_attempts:
            try:
                self.driver.find_element(by=AppiumBy.XPATH,
                                         value=element).is_displayed()
                return True
            except NoSuchElementException:
                if current_attempt == max_attempts:
                    raise
                else:
                    BasePage.swipe_down(self)
                    current_attempt += 1

    def coordinates(self, element: str):
        """Show coordinates requested element.

        :param element: str - locator from xpath list. :return: return
        coordinates by location function, when fail swipe down and search
        further.
        """
        try:
            coordinate = WebDriverWait(self.driver,
                                       timeout=BasePage.wait_time).until(
                lambda x: x.find_element(AppiumBy.XPATH, element))
            return coordinate.location
        except TimeoutError:
            print("Cant find element in requested time")
            return False

    def coordinates_are_equal(self, element1: str, element2: str) -> bool:
        """Checks if the coordinates of the elements are equal.

        :param: element1: str - locator from xpath list.
        :param: element2: str - locator from xpath list.
        :return: bool - True if element are equal, otherwise False .
        """
        try:
            location_1 = BasePage.coordinates(self, element1)
            location_2 = BasePage.coordinates(self, element2)
            if location_1['x'] == location_2['x'] and location_1['y'] == \
                    location_2['y']:
                return True
        except AttributeError:
            return False

    def click_key_event(self, key_event):
        """Click on chosen key event.

        :param key_event: int - number of key events.
        :return: press in requested key event.
        """
        try:
            WebDriverWait(self.driver, timeout=BasePage.wait_time).until(
                lambda x: x.press_keycode(key_event))
        except KeyError:
            print("Kay event not found in requested time")
            return False

    def get_reference_of_element_by_swipe_down(self, element: str):
        """Check if chosen element is visible.
        If True, return reference to element.
        :param str element: XPATH to element.
        :return: If found return reference to element, otherwise None.
        :rtype:
        """
        max_attempts = 10

        time.sleep(0.5)

        for current_attempt in range(max_attempts):
            try:

                print(f"element='{element}'")

                el = self.driver.find_element(by=AppiumBy.XPATH, value=element)
                if el.is_displayed():
                    print(f"element.is_displayed()='{el.is_displayed()}'")
                    return el
            except NoSuchElementException:
                print("NoSuchElementError")
                time.sleep(0.5)

            BasePage.swipe_down(self)
        return None

    def clear_field(self, element):
        """Clear the text from the chosen element.

        :param element: str - XPath locator for the element.
        :return: True if element is cleared successfully, False otherwise.
        """
        try:
            clear_element = WebDriverWait(self.driver,
                                          timeout=BasePage.wait_time,
                                          poll_frequency=0.1).until(
                lambda x: x.find_element(by=AppiumBy.XPATH, value=element))
            clear_element.clear()
            return True
        except TimeoutError:
            print("Timeout: Element not found.")
        except Exception as e:
            print(f"Error while clearing element: {str(e)}")
        return False

    def enable_internet(self):
        """Enable internet on emulator"""
        self.driver.execute_script('mobile: shell',
                                   {'command': "svc wifi enable"})
        self.driver.execute_script('mobile: shell',
                                   {'command': "svc data enable"})

    def disable_internet(self):
        """Disable internet on emulator"""
        self.driver.execute_script('mobile: shell',
                                   {'command': "svc wifi disable"})
        self.driver.execute_script('mobile: shell',
                                   {'command': "svc data disable"})

    def double_click(self, element):
        """Double click on requested element.

        :param element: str xpath.
        :return: execute double click on element.
        """
        double_click = TouchAction(self.driver)
        xpath = self.driver.find_element(by=AppiumBy.XPATH, value=element)
        double_click.tap(xpath, count=2)
        return double_click.perform()

    def click_coordinates(self, bounds):
        """Click on requested bounds.

        :param bounds: dict - coordinate x and y.
        :return: execute click coordinate.
        """
        click_coordinates = TouchAction(self.driver)
        return click_coordinates.tap(None, bounds["x"], bounds["y"] - 50,
                                     1).perform()
