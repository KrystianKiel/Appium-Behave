from AppiumDemo.pages.basepage import BasePage


class LoginPage(BasePage):
    login_page = "//*[@resource-id='com.skill2lead.appiumdemo:id/Login']"
    fields = {
        'email_field': "//*[@resource-id='com.skill2lead.appiumdemo:id/Et4']",
        'password_field': "//*[@resource-id='com.skill2lead.appiumdemo:id"
                          "/Et5']"
    }
    login_button = "//*[@resource-id='com.skill2lead.appiumdemo:id/Btn3']"
    wrong_credential_text = "//*[@resource-id='com.skill2lead.appiumdemo:id" \
                            "/Tv8']"

    def go_to_login(self):
        """Go to Login page"""
        BasePage.is_element_visible_by_swipe_down(
            self, LoginPage.login_page)
        BasePage.click_element(self, LoginPage.login_page)

    def put_credential(self, email, password):
        credential = [email, password]
        x = 0
        for i in LoginPage.fields:
            BasePage.is_element_visible_by_swipe_down(self, i)
            BasePage.click_element(self, i)
            BasePage.clear_field(self, i)
            BasePage.send_key(self, i, credential[x])
            x += 1
        BasePage.is_element_visible_by_swipe_down(self, LoginPage.login_button)

    def invalid_credential(self):
        BasePage.is_element_visible(self, LoginPage.wrong_credential_text)
