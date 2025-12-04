import allure
from selene import browser

from config import config


class SAASPageSelene:
    def __init__(self, driver):
        self.saas_page = config.pages["saas_page"]["url_page"]
        self.base_url = config.base_url
        self.driver = driver

    @allure.step("Открываем страницу SAAS")
    def open_page(self):
        browser.open(self.base_url + self.saas_page)
