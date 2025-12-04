import allure
from selene import browser

from config import config


class SymfonyPageSelene:
    def __init__(self, driver):

        self.symfony_page = config.pages["symfony_page"]["url_page"]
        self.base_url = config.base_url
        self.driver = driver

    @allure.step("Открываем страницу Symfony")
    def open_page(self):
        browser.open(self.base_url + self.symfony_page)
