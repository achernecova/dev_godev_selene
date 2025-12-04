import allure
import pytest
from allure_commons.types import Severity

from pages.services_page_selene import ServicesPageSelene


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "chernetsova")
@allure.feature("Открытие страниц при переходе из блока Services -> service-item")
@allure.story("Открытие страниц блока Services")
@allure.link("https://godev.agency/", name="Testing")
@pytest.mark.parametrize(
    "index, name_page, title_page",
    [
        (1, "mobile_page", "Application development services"),
        (2, "website_dev_page", "Website development"),
        (3, "tech_support_page", "Maintenance and Support"),
        (4, "custom_software_dev_page", "Custom software development services"),
        (5, "web_development_page", "Web development services"),
        (6, "e_com_page", "E-commerce web development for scalable business growth"),
        (7, "website_design_page", "Website design and development services"),
        (8, "outstaff_page", "IT Staff Augmentation"),
    ],
    ids=[
        "mobile_page",
        "website_dev_page",
        "tech_support",
        "custom_software_dev_page",
        "web_development",
        "e_com",
        "website_design",
        "outstaff",
    ],
)
def test_service_page_service_item_block_open_page_card_more(
    index, name_page, title_page
):

    with allure.step("Открываем главную страницу"):
        page = ServicesPageSelene()
        page.open_page()

    with allure.step(f"Открываем страницу '{name_page}' из блока Services"):
        page.open_page_from_services_block_by_index(index)

    with allure.step("Проверяем URL и заголовок страницы"):
        page.check_page_url_and_title(name_page, title_page)


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
            "project_mint_link",
            "Enhancing Mint Link’s MICE platform for optimal user engagement",
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
            "project_vegan_hotel",
            "Website development for a conceptual hotel in the Dolomites",
        ),
    ],
    ids=["euro_vpn", "mint_link", "find_a_builder", "sls", "vegan_hotel"],
)
def test_services_page_project_open_page_card_more(index, page_name, title_page):
    # открыли страницу
    with allure.step("Открываем главную страницу"):
        page = ServicesPageSelene()
        page.open_page()

    with allure.step(f"Открываем страницу '{page_name}' из блока Project"):
        page.open_page_from_project_block_by_index(index)

    with allure.step("Проверяем URL и заголовок страницы"):
        page.check_page_url_and_title(page_name, title_page)
