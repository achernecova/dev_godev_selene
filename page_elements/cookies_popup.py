from selene import be, browser


class CookiesPopup:

    @staticmethod
    def close_modal():
        element_close_modal = browser.element(".close-modal").should(be.visible)
        element_close_modal.click()
