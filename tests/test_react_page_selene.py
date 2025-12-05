# import allure
# import pytest
# from allure_commons.types import Severity
#
# from pages.react_page_selene import ReactPageSelene
#
#
# @allure.tag("critical")
# @allure.severity(Severity.CRITICAL)
# @allure.label("owner", "chernetsova")
# @allure.feature("Открытие страниц при переходе из блока Project")
# @allure.story("Открытие страниц блока Project")
# @allure.link("https://godev.agency/", name="Testing")
# @pytest.mark.parametrize(
#     "index, page_name, title_page",
#     [
#         (1, "symfony_page", "Symfony development services"),
#         (2, "codeigniter_page", "CodeIgniter development company"),
#         (3, "python_page", "Python development services for scalable solutions"),
#     ],
#     ids=["symfony", "codeigniter", "python"],
# )
# def test_react_page_block_other_services_open_page(index, page_name, title_page):
#     # открыли страницу
#     with allure.step("Открываем главную страницу"):
#         page = ReactPageSelene()
#         page.open_page()
#
#     with allure.step(f"Открываем страницу '{page_name}' из блока Other services for you"):
#         page.open_page_from_other_services_by_index(index)
#
#     with allure.step("Проверяем URL и заголовок страницы"):
#         page.check_page_url_and_title(page_name, title_page)
