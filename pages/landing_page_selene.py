import allure
from selene import browser, have

from config import config
from page_elements.block_other_services import BlockOtherServices
from page_elements.block_project_element import BlockProjectElement
from page_elements.cookies_popup import CookiesPopup
from page_elements.metadata_elements import MetaDataElements
from page_elements.scroll_element_selene import ScrollElement
from page_elements.service_item_block_selene import ServiceItemBlockSelene
from page_elements.website_packages_block_selene import WebSitePackagesBlockSelene


class LandingPageSelene:
    def __init__(self):
        self.landing_page = config.pages["landing_page"]["url_page"]
        self.base_url = config.base_url
        self.metadata_helper = MetaDataElements()
        self.service_item_block_card_more = ServiceItemBlockSelene()
        self.cookie_modal = CookiesPopup()
        self.block_project = BlockProjectElement()
        self.block_website_packages_more = WebSitePackagesBlockSelene()
        self.scroll_element = ScrollElement()
        self.block_other_services = BlockOtherServices()

    @allure.step("Открываем главную страницу")
    def open_page(self):
        browser.open(self.base_url + self.landing_page)

    @allure.step("Проверяем URL и заголовок страницы")
    def check_page_url_and_title(self, page_name, title_page):
        current_page_data = config.get_page_data(page_name)
        browser.should(
            have.url(current_page_data["url_page"])
        )  # 'url_page' - ключ в словаре, где хранится URL
        browser.element("h1").should(have.exact_text(title_page))

    @allure.step("Открываем {value} из блока 'Project'")
    def open_page_from_project_block_by_index(self, value):
        self.scroll_element.scroll_to_element("(//*[@class='projects-item'])", value)
        self.cookie_modal.close_modal()
        more_buttons = self.block_project.button_project()
        more_buttons[value - 1].click()
