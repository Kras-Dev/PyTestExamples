# pages/personal_page.py

import allure
from base.base_page import BasePage
from config.url_config import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class PersonalPage(BasePage):
    PAGE_URL = Links.PERSONAL_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")

    def change_name(self, new_name):
        with allure.step(f"Change name on '{new_name}'"):
            self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            first_name_field.click()
            self.driver.execute_script("arguments[0].value = ''", first_name_field)            
            #first_name_field.clear()
            assert first_name_field.get_attribute("value") == "", "First name field is not empty"
            first_name_field.send_keys(new_name)
            #self.name = new_name
            return new_name

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.visibility_of_element_located(self.SAVE_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Changes saved successfully")
    def changes_check(self, new_name):
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, new_name))