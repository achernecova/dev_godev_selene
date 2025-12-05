import allure
import pytest
from allure_commons.types import Severity

from pages.framework_page_selene import FrameworkPageSelene


@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "chernetsova")
@allure.feature("Открытие страниц при переходе из блока Project")
@allure.story("Открытие страниц блока Project")
@allure.link("https://godev.agency/", name="Testing")
@pytest.mark.parametrize(
    "index, page_name, title_page",
    [
        (
            1,
            "project_find_a_builder",
            "Website development for London construction company",
        ),
        (
            2,
            "project_vegan_hotel",
            "Website development for a conceptual hotel in the Dolomites",
        ),
    ],
    ids=["find_a_builder", "vegan_hotel"],
)
def test_framework_page_project_open_page_card_more(index, page_name, title_page):
    with allure.step("Открываем главную страницу"):
        page = FrameworkPageSelene()
        page.open_page()
    with allure.step(f"Открываем страницу '{page}' из блока Project"):
        page.open_page_from_project_block_by_index(index)
    with allure.step("Проверяем URL и заголовок страницы"):
        page.check_page_url_and_title(page_name, title_page)
