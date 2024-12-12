# pages/dashboard_page.py

import allure
from base.base_page import BasePage
from config.url_config import Links
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage(BasePage):
    PAGE_URL = Links.DASHBOARD_PAGE

    MY_INFO_BUTTON = ("xpath", "//span[text()='My Info']")

    @allure.step("Click on 'My Info' Link")
    def click_my_info_button(self):
        self.wait.until(EC.visibility_of_element_located(self.MY_INFO_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()