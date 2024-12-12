# base/base_page.py

import allure
from allure_commons.types import AttachmentType 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver):
        # Инициализируем класс с драйвером
        self.driver = driver
        # Создаем объект WebDriverWait для ожидания с максимальным временем 10 секунд и частотой проверки 1 секунда
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)
        
    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
        # Открываем URL-адрес страницы
            self.driver.get(self.PAGE_URL)
    
    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is open"):
         # Проверяем, что текущий URL соответствует ожидаемому URL-адресу страницы
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )


