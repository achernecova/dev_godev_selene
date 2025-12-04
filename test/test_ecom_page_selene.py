import allure
import pytest
from allure_commons.types import Severity

from pages.e_com_page_selene import EComPageSelene


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
    ],
    ids=["euro_vpn", "vegan_hotel", "find_a_builder", "sls"],
)
def test_ecom_page_project_open_page_card(index, page_name, title_page):
    # открыли страницу
    with allure.step("Открываем главную страницу"):
        page = EComPageSelene()
        page.open_page()

    with allure.step(f"Открываем страницу '{page_name}' из блока Project"):
        page.open_page_from_project_block_by_index(index)

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
        (1, "cms_page", "Custom CMS development service"),
        (2, "b2b_page", "B2B e-commerce website development"),
        (3, "custom_software_dev_page", "Custom software development services"),
    ],
    ids=["cms_page", "b2b_page", "custom_software_dev_page"],
)
def test_ecom_page_block_other_services_open_page(index, page_name, title_page):
    # открыли страницу
    with allure.step("Открываем главную страницу"):
        page = EComPageSelene()
        page.open_page()

    with allure.step(f"Открываем страницу '{page_name}' из блока Other services for you"):
        page.open_page_from_other_services_by_index(index)

    with allure.step("Проверяем URL и заголовок страницы"):
        page.check_page_url_and_title(page_name, title_page)
