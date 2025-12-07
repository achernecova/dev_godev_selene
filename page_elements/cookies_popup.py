from selene import be, browser
from selenium.webdriver.common.by import By


class CookiesPopup:

    @staticmethod
    def close_modal():
        browser.element((By.TAG_NAME, "body")).click()
        element_close_modal = browser.element(".close-modal").should(be.visible)
        element_close_modal.click()
