import allure
from selene import browser, have

from config import config
from page_elements.block_project_element import BlockProjectElement
from page_elements.cookies_popup import CookiesPopup
from page_elements.metadata_elements import MetaDataElements
from page_elements.scroll_element_selene import ScrollElement
from page_elements.service_item_block_selene import ServiceItemBlockSelene


class ServicesPageSelene:
    def __init__(self):
        self.base_url = config.base_url
        self.services_page = config.pages["services_page"]["url_page"]
        self.cookie_modal = CookiesPopup()
        self.metadata_helper = MetaDataElements()
        self.service_item_block_card_more = ServiceItemBlockSelene()
        self.block_project = BlockProjectElement()
        self.scroll_element = ScrollElement()

    def get_meta_description(self) -> str:
        return self.metadata_helper.get_meta_description()

    def open(self):
        browser.open(self.services_page)

    def get_meta_canonical(self) -> str:
        return self.metadata_helper.get_canonical_url()

    def close_cookies(self):
        return self.cookie_modal.close_modal()

    @allure.step("Открываем главную страницу")
    def open_page(self):
        browser.open(self.base_url + self.services_page)

    @allure.step("Открываем страницу из блока 'Services'")
    def open_page_from_services_block_by_index(self, index):
        more_buttons = self.service_item_block_card_more.more_buttons()
        self.scroll_element.scroll_to_element("(//*[@class='service-item']//a)", index)
        self.close_cookies()
        self.scroll_element.scroll_to_element("(//*[@class='service-item']//a)", index)
        more_buttons[index - 1].click()

    @allure.step("Проверяем URL и заголовок страницы")
    def check_page_url_and_title(self, page_name, title_page):
        current_page_data = config.get_page_data(page_name)
        browser.should(
            have.url(current_page_data["url_page"])
        )  # 'url_page' - ключ в словаре, где хранится URL
        browser.element("h1").should(have.exact_text(title_page))

    @allure.step("Открываем проект из блока 'Project'")
    def open_page_from_project_block_by_index(self, value):
        self.scroll_element.scroll_to_element("(//*[@class='projects-item'])", value)
        self.cookie_modal.close_modal()
        self.scroll_element.scroll_to_element("(//*[@class='projects-item'])", value)
        more_buttons = self.block_project.button_project()
        more_buttons[value - 1].click()
