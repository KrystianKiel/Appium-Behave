from AppiumDemo.pages.basepage import BasePage


class TabActivity(BasePage):
    tab_activity = "//*[@resource-id='com.skill2lead.appiumdemo:id/TabView']"
    home_fragment = "//*[@text='Home fragment']"
    sport_fragment = "//*[@text='Sport fragment']"
    movie_fragment = "//*[@text='Movie fragment']"

    def go_to_tabactivity(self):
        """Go to TabActivity page"""
        BasePage.is_element_visible_by_swipe_down(
            self, TabActivity.tab_activity)
        BasePage.click_element(self, TabActivity.tab_activity)

    def swipe_to_movie(self):
        while not BasePage.is_element_visible(
                self, TabActivity.movie_fragment):
            BasePage.swipe_right(self)

    def swipe_to_home(self):
        while not BasePage.is_element_visible(
                self, TabActivity.home_fragment):
            BasePage.swipe_left(self)
