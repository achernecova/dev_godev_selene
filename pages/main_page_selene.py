import allure
from selene import browser, have
from selenium.webdriver.common.by import By

from config import config
from page_elements.block_project_element import BlockProjectElement
from page_elements.cookies_popup import CookiesPopup
from page_elements.metadata_elements import MetaDataElements
from page_elements.popup_form import PopupFormRequests
from page_elements.scroll_element_selene import ScrollElement
from page_elements.service_item_block_selene import ServiceItemBlockSelene
from page_elements.website_packages_block_selene import WebSitePackagesBlockSelene


class MainPageSelene:
    def __init__(self):
        self.base_url = config.base_url  # Сохраняем base_url в атрибут класса
        self.metadata_helper = MetaDataElements()
        self.service_item_block_card_more = ServiceItemBlockSelene()
        self.cookie_modal = CookiesPopup()
        self.block_project = BlockProjectElement()
        self.block_website_packages_more = WebSitePackagesBlockSelene()
        self.scroll_element = ScrollElement()
        self.popup_requests = PopupFormRequests()

    def get_meta_description(self) -> str:
        return self.metadata_helper.get_meta_description()

    def get_meta_canonical(self) -> str:
        return self.metadata_helper.get_canonical_url()

    @allure.step("Открываем {value} из блока 'Project'")
    def open_page_from_project_block_by_index(self, value):
        browser.element((By.TAG_NAME, "body")).click()
        self.scroll_element.scroll_to_element("(//*[@class='projects-item'])", value)
        self.cookie_modal.close_modal()
        self.scroll_element.scroll_to_element("(//*[@class='projects-item'])", value)
        more_buttons = self.block_project.button_project()
        more_buttons[value - 1].click()

    @allure.step("Открываем страницу из блока 'Website Packages'")
    def open_page_from_website_packages_block_by_index(self, value):
        self.scroll_element.scroll_to_element("(//*[@class='team-card'])", value)
        self.cookie_modal.close_modal()
        self.scroll_element.scroll_to_element("(//*[@class='team-card'])", value)
        more_buttons = self.block_website_packages_more.button_website_packages_more()
        more_buttons[value - 1].click()

    @allure.step("Проверяем URL и заголовок страницы")
    def check_page_url_and_title(self, page_name, title_page):
        current_page_data = config.get_page_data(page_name)
        browser.should(
            have.url(current_page_data["url_page"])
        )  # 'url_page' - ключ в словаре, где хранится URL
        browser.element("h1").should(have.exact_text(title_page))

    @allure.step("Открываем страницу из блока 'Services'")
    def open_page_from_services_block_by_index(self, value):
        self.scroll_element.scroll_to_element("(//*[@class='service-item']//a)", value)
        self.cookie_modal.close_modal()
        self.scroll_element.scroll_to_element("(//*[@class='service-item']//a)", value)
        more_buttons = self.service_item_block_card_more.more_buttons()
        more_buttons[value - 1].click()

    def open_page(self):
        browser.open(self.base_url)
