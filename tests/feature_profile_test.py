# tests/feature_profile_test.py

import allure
import pytest
import random
from base.base_test import BaseTest
# Файл conf_test.py является специальным файлом в pytest, который автоматически распознается и загружается для всех
# тестов в директории и поддиректориях.
from conf_test import driver

@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):
    
    @allure.title("Change Profile data")
    @allure.severity("Minor")
    @pytest.mark.smoke
    @pytest.mark.parametrize("new_name", [f"Test {random.randint(1, 100)}" for _ in range(1)])
    def test_change_profile_name(self, new_name):
        self.login_page.open()
        self.login_page.input_login(self.data.LOGIN)
        self.login_page.input_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()

        self.dashboard_page.click_my_info_button()
        self.personal_page.is_opened()

        #self.personal_page.change_name(f"Test {random.randint(1,100)}")
        self.personal_page.change_name(new_name)
        self.personal_page.save_changes()
        self.personal_page.changes_check(new_name)
