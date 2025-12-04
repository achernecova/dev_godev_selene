import allure
from selene import browser

from config import config


class PythonPageSelene:
    def __init__(self, driver):
        self.python_page = config.pages["python_page"]["url_page"]
        self.base_url = config.base_url
        self.driver = driver

    @allure.step("Открываем страницу Python")
    def open_page(self):
        browser.open(self.base_url + self.python_page)
