from time import sleep

from selene import be, browser
from selenium.webdriver.common.by import By


class CookiesPopup:

    @staticmethod
    def close_modal():
        browser.element((By.TAG_NAME, "body")).click()
        element_close_modal = browser.element(".close-modal").should(be.visible).click()
        if element_close_modal.should(be.not_.visible):
            print("Окно куков закрыто")
        else:
            print("Окно не закрыто")

