from selene import browser

from page_elements.metadata_elements import MetaDataElements


class MobilePageSelene:
    def __init__(self):
        self.metadata_helper = MetaDataElements()

    def get_meta_description(self) -> str:
        return self.metadata_helper.get_meta_description()

    def get_meta_canonical(self) -> str:
        return self.metadata_helper.get_canonical_url()

    @staticmethod
    def open_page(value):
        browser.open(value)
