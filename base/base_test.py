# base/base_test.py
import allure
import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.personal_page import PersonalPage

class BaseTest:
    data: Data
    # Объявление переменных для страниц
    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_page: PersonalPage

    # Фикстура pytest (автоматически применяется к тестам в этом классе)
    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        with allure.step(f"Set up web driver"):
            request.cls.data = Data()
            # Сохранение драйвера в класс для доступа в тестах
            request.cls.driver = driver
            # Инициализация объектов страниц с использованием драйвера
            request.cls.login_page = LoginPage(driver)
            request.cls.dashboard_page = DashboardPage(driver)
            request.cls.personal_page = PersonalPage(driver)