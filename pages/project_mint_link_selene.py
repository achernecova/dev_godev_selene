from selene import browser

from page_elements.cookies_popup import CookiesPopup
from page_elements.metadata_elements import MetaDataElements
from page_elements.service_item_block_selene import ServiceItemBlockSelene


class ProjectMintLinkSelene:
    def __init__(self):
        self.metadata_helper = MetaDataElements()
        self.service_item_block_card_more = ServiceItemBlockSelene()
        self.cookie_modal = CookiesPopup()

    def get_meta_description(self) -> str:
        return self.metadata_helper.get_meta_description()

    def get_meta_canonical(self) -> str:
        return self.metadata_helper.get_canonical_url()

    @staticmethod
    def open_page(value):
        browser.open(value)
