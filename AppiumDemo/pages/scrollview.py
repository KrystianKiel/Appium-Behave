from AppiumDemo.pages.basepage import BasePage


class ScrollView(BasePage):
    ScrollView = "//*[@resource-id='com.skill2lead.appiumdemo:id/ScrollView']"
    Button16 = "//*[@text='BUTTON16']"
    Alert = "//*[@resource-id='com.skill2lead.appiumdemo:id/alertTitle']"
    Yes_button = "//*[@resource-id='android:id/button1']"

    def go_to_scrollview(self):
        """Go to ScrollView page"""
        BasePage.is_element_visible_by_swipe_down(self,
                                                  ScrollView.ScrollView)
        BasePage.click_element(self, ScrollView.ScrollView)
