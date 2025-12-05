import allure
from selene import browser, have

from config import config
from page_elements.block_other_services import BlockOtherServices
from page_elements.block_project_element import BlockProjectElement
from page_elements.cookies_popup import CookiesPopup
from page_elements.metadata_elements import MetaDataElements
from page_elements.scroll_element_selene import ScrollElement
from page_elements.website_packages_block_selene import WebSitePackagesBlockSelene


class WebSiteDevPage:
    def __init__(self):
        self.website_dev_page = config.pages["website_dev_page"]["url_page"]
        self.base_url = config.base_url
        self.metadata_helper = MetaDataElements()
        self.cookie_modal = CookiesPopup()
        self.block_project = BlockProjectElement()
        self.block_website_packages_more = WebSitePackagesBlockSelene()
        self.scroll_element = ScrollElement()
        self.block_other_services = BlockOtherServices()
        self.locator_team_card = "(//*[@class='team-card'])"
        self.locator_project_team = "(//*[@class='projects-item'])"

    def get_meta_description(self) -> str:
        return self.metadata_helper.get_meta_description()

    def get_meta_canonical(self) -> str:
        return self.metadata_helper.get_canonical_url()

    @allure.step("Открываем страницу")
    def open_page(self):
        """Открывает главную страницу сайта."""
        browser.open(self.base_url + self.website_dev_page)

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

    @allure.step("Открываем {value} из блока 'Project'")
    def open_page_from_project_block_by_index(self, value):
        self.scroll_element.scroll_to_element(self.locator_project_team, value)
        self.cookie_modal.close_modal()
        self.scroll_element.scroll_to_element(self.locator_project_team, value)
        more_buttons = self.block_project.button_project()
        more_buttons[value - 1].click()
