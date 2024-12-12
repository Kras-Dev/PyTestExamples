# conf_test.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Используем декоратор pytest.fixture для определения фикстуры 'driver'
# scope="function" означает, что фикстура будет создаваться для каждой функции-теста
# autouse=True означает, что фикстура будет автоматически применяться ко всем тестам без явного указания
@pytest.fixture(scope="function", autouse=True) #function
def driver(request):
    # Код, который выполняется перед тестом
    options = Options()  # Создаем объект Options для настройки параметров Chrome 
    #options.add_argument("--headless") # Для запуска браузера в безголовом режиме (без GUI)
    options.add_argument("--no-sandbox") # Отключаем использование песочницы, что может быть необходимо в некоторых средах (например, в Docker)
    options.add_argument("--disable-dev-shm-usage") # Отключаем использование /dev/shm, что может предотвратить ошибки с памятью в контейнерах
    #options.add_argument("--window-size=1200,640")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver # Сохраняем драйвер в объект запроса для доступа к нему в тестах
    driver.maximize_window()

    yield driver # Здесь тест будет выполняться # Возвращаем управление тесту, позволяя ему работать с драйвером

    # Код, который выполняется после теста
    driver.quit()