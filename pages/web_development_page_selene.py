from selene import browser

from page_elements.cookies_popup import CookiesPopup
from page_elements.metadata_elements import MetaDataElements


class WebDevelopmentPageSelene:
    def __init__(self):
        self.metadata_helper = MetaDataElements()
        self.cookie_modal = CookiesPopup()

    def get_meta_description(self) -> str:
        return self.metadata_helper.get_meta_description()

    def get_meta_canonical(self) -> str:
        return self.metadata_helper.get_canonical_url()

    def open_page(self, value):
        browser.open(value)

    def close_cookies(self):
        return self.cookie_modal.close_modal()
