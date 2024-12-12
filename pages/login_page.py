# pages/login_page.py

import allure
from base.base_page import BasePage
from config.url_config import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")

    @allure.step("Input Login")
    def input_login(self, login):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD))
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)
             
    @allure.step("Input Password")
    def input_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD))
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Click Submit Button")
    def click_submit_button(self):
        # self.wait.until(EC.visibility_of_element_located(self.SUBMIT_BUTTON))
        # self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))#.click()
        # ActionChains(self.driver).move_to_element(self.SUBMIT_BUTTON).click().perform()
        
        submit_button = self.wait.until(EC.visibility_of_element_located(self.SUBMIT_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))
        ActionChains(self.driver).move_to_element(submit_button).click().perform()