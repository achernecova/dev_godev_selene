import allure
import pytest
from allure_commons.types import Severity

from config import config
from pages.d2c_page_selene import D2CPageSelene


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "chernetsova")
@allure.feature("Открытие страниц при переходе из блока Website Packages -> team-card")
@allure.story("Открытие страниц блока Website Packages")
@allure.link("https://godev.agency/", name="Testing")
@pytest.mark.parametrize(
    "index, page_name, title_page",
    [
        (1, "e_com_page", "E-commerce web development for scalable business growth"),
        (2, "landing_page", "Mastering landing page design in the USA"),
        (3, "b2b_page", "B2B e-commerce website development"),
        (
            4,
            "framework_page",
            "What is a framework and why it’s essential for web development",
        ),
    ],
    ids=["e_com", "landing_page", "b2b_page", "framework_page"],
)
def test_d2c_page_website_packages_block_open_page(index, page_name, title_page):
    base_page_data = config.get_page_data("base_page")

    with allure.step("Открываем главную страницу"):
        page = D2CPageSelene()
        page.open_d2c_page(base_page_data["url_page"])

    with allure.step(f"Открываем страницу '{page_name}' из блока Website Packages"):
        page.open_page_from_website_packages_block_by_index(index)

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
def test_d2c_page_project_open_page_card_more(index, page_name, title_page):
    with allure.step("Открываем главную страницу"):
        page = D2CPageSelene()
        page.open_page()

    with allure.step(f"Открываем страницу '{page_name}' из блока Project"):
        page.open_page_from_project_block_by_index(index)

    with allure.step("Проверяем URL и заголовок страницы"):
        page.check_page_url_and_title(page_name, title_page)


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "chernetsova")
@allure.feature("Открытие страниц при переходе из блока Other services for you")
@allure.story("Открытие страниц блока Project")
@allure.link("https://godev.agency/", name="Testing")
@pytest.mark.parametrize(
    "index, page_name, title_page",
    [
        (1, "saas_page", "SaaS Development Services"),
        (2, "e_com_page", "E-commerce web development for scalable business growth"),
        (3, "outstaff_page", "IT Staff Augmentation"),
    ],
    ids=["saas_page", "e_com_page", "outstaff_page"],
)
def test_d2c_page_block_other_services_open_page(index, page_name, title_page):
    # открыли страницу
    with allure.step("Открываем главную страницу"):
        page = D2CPageSelene()
        page.open_page()

    with allure.step(f"Открываем страницу '{page_name}' из блока Other services for you"):
        page.open_page_from_other_services_by_index(index)

    with allure.step("Проверяем URL и заголовок страницы"):
        page.check_page_url_and_title(page_name, title_page)
