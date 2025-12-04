import allure
from selene import browser

from config import config


class CodeigniterPageSelene:
    def __init__(self, driver):
        self.codeigniter_page = config.pages["codeigniter_page"]["url_page"]
        self.base_url = config.base_url
        self.driver = driver

    @allure.step("Открываем страницу Codeigniter")
    def open_page(self):
        browser.open(self.base_url + self.codeigniter_page)
