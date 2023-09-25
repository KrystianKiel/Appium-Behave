from AppiumDemo.pages.basepage import BasePage


class ContactUsForm(BasePage):
    contact_us_form = "//*[@resource-id='com.skill2lead.appiumdemo:id" \
                      "/ContactUs']"
    text_boxes = {
        'Name': "//*[@resource-id='com.skill2lead.appiumdemo:id/Et2']",
        'Email': "//*[@resource-id='com.skill2lead.appiumdemo:id/Et3']",
        'Address': "//*[@resource-id='com.skill2lead.appiumdemo:id/Et6']",
        'Mobile': "//*[@resource-id='com.skill2lead.appiumdemo:id/Et7']"
    }
    output_boxes = {
        'Name': "//*[@resource-id='com.skill2lead.appiumdemo:id/Tv2']",
        'Email': "//*[@resource-id='com.skill2lead.appiumdemo:id/Tv7']",
        'Address': "//*[@resource-id='com.skill2lead.appiumdemo:id/Tv5']",
        'Mobile': "//*[@resource-id='com.skill2lead.appiumdemo:id/Tv6']"
    }

    def go_to_contactusform(self):
        """Go to ContactUsForm page"""
        BasePage.is_element_visible_by_swipe_down(
            self, ContactUsForm.contact_us_form)
        BasePage.click_element(self, ContactUsForm.contact_us_form)

    def put_value(self, value1, value2, value3, value4):
        """Put value at ContactUsForm page"""
        values = [value1, value2, value3, value4]
        i = 0
        for key in ContactUsForm.text_boxes:
            value = ContactUsForm.text_boxes[key]
            BasePage.is_element_visible_by_swipe_down(self, value)
            BasePage.click_element(self, value)
            BasePage.clear_field(self, value)
            BasePage.send_key(self, value, values[i])
            i += 1

    def check_if_value_valid(self):
        """Check if value is equal to output, on ContactUsForm page"""
        BasePage.is_element_visible_by_swipe_down(self,
                                                  BasePage.submit)
        BasePage.click_element(self, BasePage.submit)
        for key in ContactUsForm.text_boxes:
            text_locator = ContactUsForm.text_boxes[key]
            output_locator = ContactUsForm.output_boxes[key]
            assert BasePage.text(self, text_locator) in BasePage.text(
                self, output_locator)
