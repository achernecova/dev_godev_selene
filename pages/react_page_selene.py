import allure
from selene import browser, have

from config import config
from page_elements.block_other_services import BlockOtherServices
from page_elements.block_project_element import BlockProjectElement
from page_elements.cookies_popup import CookiesPopup
from page_elements.metadata_elements import MetaDataElements
from page_elements.scroll_element_selene import ScrollElement
from page_elements.service_item_block_selene import ServiceItemBlockSelene


class ReactPageSelene:
    def __init__(self):
        self.reactjs_page = config.pages["reactjs_page"]["url_page"]
        self.base_url = config.base_url
        self.block_project = BlockProjectElement()
        self.block_other_services = BlockOtherServices()
        self.scroll_element = ScrollElement()
        self.metadata_helper = MetaDataElements()
        self.service_item_block_card_more = ServiceItemBlockSelene()
        self.cookie_modal = CookiesPopup()

    def get_meta_description(self) -> str:
        return self.metadata_helper.get_meta_description()

    def get_meta_canonical(self) -> str:
        return self.metadata_helper.get_canonical_url()

    @allure.step("Открываем главную страницу")
    def open_page(self):
        """Открывает главную страницу сайта."""
        browser.open(self.base_url + self.reactjs_page)

    def open_page_from_other_services_by_index(self, value):
        self.scroll_element.scroll_element_to_center()
        self.cookie_modal.close_modal()
        self.scroll_element.scroll_element_to_center()
        more_buttons = self.block_other_services.button_other_services_more()
        more_buttons[value - 1].click()

    @allure.step("Проверяем URL и заголовок страницы")
    def check_page_url_and_title(self, page_name, title_page):
        current_page_data = config.get_page_data(page_name)
        browser.should(
            have.url(current_page_data["url_page"])
        )  # 'url_page' - ключ в словаре, где хранится URL
        browser.element("h1").should(have.exact_text(title_page))
