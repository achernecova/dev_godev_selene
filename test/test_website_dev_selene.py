import allure
import pytest
from allure_commons.types import Severity

from pages.website_dev_page import WebSiteDevPage


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "chernetsova")
@allure.feature("Открытие страниц при переходе из блока Other services")
@allure.story("Открытие страниц блока Other services")
@allure.link("https://godev.agency/", name="Testing")
@pytest.mark.parametrize(
    "index, page_name, title_page",
    [
        (1, "website_design_page", "Website design and development services"),
        (2, "website_dev_page", "Website development"),
        (3, "website_design_page", "Website design and development services"),
    ],
    ids=["design1", "website_dev", "design2"],
)
def test_website_dev_page_block_other_services_open_page(index, page_name, title_page):
    # открыли страницу
    with allure.step("Открываем главную страницу"):
        page = WebSiteDevPage()
        page.open_page()

    with allure.step(f"Открываем страницу '{page_name}' из блока Other services for you"):
        page.open_page_from_other_services_by_index(index)

    with allure.step("Проверяем URL и заголовок страницы"):
        page.check_page_url_and_title(page_name, title_page)


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "chernetsova")
@allure.feature("Открытие страниц при переходе из блока Project")
@allure.story("Открытие страниц блока Project")
@allure.link("https://godev.agency/", name="Testing")
@pytest.mark.parametrize(
    "index, page_name, title_page",
    [
        (1, "project_euro_vpn", "Information security service redesign"),
        (
            2,
            "project_vegan_hotel",
            "Website development for a conceptual hotel in the Dolomites",
        ),
        (
            3,
            "project_find_a_builder",
            "Website development for London construction company",
        ),
        (
            4,
            "project_sls",
            "Building a robust logistics platform for Swift Logistic Solutions",
        ),
        (
            5,
            "project_mint_link",
            "Enhancing Mint Link’s MICE platform for optimal user engagement",
        ),
    ],
    ids=["euro_vpn", "vegan_hotel", "find_a_builder", "sls", "mint_link"],
)
def test_website_dev_page_project_open_page_card_more(index, page_name, title_page):

    with allure.step("Открываем главную страницу"):
        page = WebSiteDevPage()
        page.open_page()

    with allure.step(f"Открываем страницу '{page_name}' из блока Project"):
        page.open_page_from_project_block_by_index(index)

    with allure.step("Проверяем URL и заголовок страницы"):
        page.check_page_url_and_title(page_name, title_page)
