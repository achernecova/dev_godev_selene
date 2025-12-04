from selene import browser, command

from page_elements.metadata_elements import MetaDataElements


class TechSupportPageSelene:
    def __init__(self):
        self.metadata_helper = MetaDataElements()

    def get_meta_description(self) -> str:
        return self.metadata_helper.get_meta_description()

    def get_meta_canonical(self) -> str:
        return self.metadata_helper.get_canonical_url()

    @staticmethod
    def open_page(value):
        browser.open(value)

    @staticmethod
    def scroll_in_page_element():
        browser.element("#services").perform(command.js.scroll_into_view)
