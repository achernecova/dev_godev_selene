import allure
import pytest
from allure_commons.types import Severity
from selene import browser, have

from config import config
from page_elements.metadata_elements import MetaDataElements
from pages.main_page_selene import MainPageSelene

@allure.feature("Добавление метатегов на страницы")
class TestMetaDataPage:

    @allure.tag("critical")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "chernetsova")
    @allure.link("https://github.com", name="Testing")
    def test_page_meta_data(self):
        error_messages = []  # Локальный список для хранения сообщений об ошибках

        for page_name, page_data in config.pages.items():
            url = page_data["url_page"]
            title = page_data["title"]
            description = page_data["description"]

            with allure.step(f"Проверка страницы {page_name}"):
                try:
                    with allure.step(f"Открываем страницу {url}"):
                        browser.open(url)
                        print(url)

                    with allure.step(f"Проверка title страницы {page_name}"):
                        browser.should(have.title(title))

                    with allure.step(f"Проверка description страницы {page_name}"):
                        actual_description = MetaDataElements.get_meta_description()
                        assert (
                                actual_description == description
                        ), f"Ошибка в description для страницы {page_name}: ожидалось '{description}', получено '{actual_description}'"

                    with allure.step(f"Проверка canonical страницы {page_name}"):
                        actual_canonical = MetaDataElements.get_canonical_url()
                        assert (
                                actual_canonical == url
                        ), f"Ошибка в canonical для страницы {page_name}: ожидалось '{url}', получено '{actual_canonical}'"

                except Exception as e:
                    error_message = f"Ошибка при проверке страницы {page_name}: {e}"
                    error_messages.append(
                        error_message
                    )  # Добавляем сообщение об ошибке в локальный список
                    allure.attach(
                        str(e),
                        name=f"Ошибка на странице {page_name}",
                        attachment_type=allure.attachment_type.TEXT,
                    )
                    print(error_message)

        if error_messages:
            with allure.step("Итоговый статус теста: ПРОВАЛЕН"):
                allure.attach(
                    "\n".join(error_messages),
                    name="Все ошибки",
                    attachment_type=allure.attachment_type.TEXT,
                )
                pytest.fail(
                    f"Тест провален: обнаружены ошибки на следующих страницах:\n{chr(10).join(error_messages)}"
                )


@allure.feature("Открытие страниц из разных блоков страницы")
class TestLinkOpenPage:
    @allure.tag("critical")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "chernetsova")
    @allure.link("https://godev.agency/", name="Testing")
    @allure.title("Открытие страниц блока Website Packages")
    @allure.story("Линковка в блоке Website Packages")
    @pytest.mark.parametrize(
        "index, page_name, expected_title",
        [
            (1, "e_com_page", "E-commerce web development for scalable business growth"),
            (2, "b2b_page", "B2B e-commerce website development"),
            (3, "framework_page", "What is a framework and why it’s essential for web development"),
        ],
        ids=["e_com", "b2b", "framework"],
    )
    def test_main_page_website_packages_block_open_page(self, index, page_name, expected_title):
        with allure.step("Открываем главную страницу"):
            page = MainPageSelene()
            page.open_page()
        with allure.step(f"Открываем страницу '{page_name}' из блока Website Packages"):
            page.open_page_from_website_packages_block_by_index(index)
        with allure.step("Проверяем URL и заголовок страницы"):
            page.check_page_url_and_title(page_name, expected_title)

    # @allure.tag("critical")
    # @allure.severity(Severity.CRITICAL)
    # @allure.label("owner", "chernetsova")
    # @allure.story("Открытие страниц блока App and Web Development Services")
    # @allure.link("https://godev.agency/", name="Testing")
    # @pytest.mark.parametrize(
    #     "index, name_page, title_page",
    #     [
    #         (1, "mobile_page", "Application development services"),
    #         (2, "website_dev_page", "Website development"),
    #         (3, "tech_support_page", "Maintenance and Support"),
    #         (4, "custom_software_dev_page", "Custom software development services"),
    #         (5, "web_development_page", "Web development services"),
    #         (6, "e_com_page", "E-commerce web development for scalable business growth"),
    #         (7, "website_design_page", "Website design and development services"),
    #         (8, "outstaff_page", "IT Staff Augmentation"),
    #         (9, "b2b_page", "B2B e-commerce website development"),
    #         (
    #             10,
    #             "framework_page",
    #             "What is a framework and why it’s essential for web development",
    #         ),
    #     ],
    #     ids=[
    #         "mobile_page",
    #         "website_dev_page",
    #         "tech_support",
    #         "custom_software_dev_page",
    #         "web_development",
    #         "e_com",
    #         "website_design",
    #         "outstaff",
    #         "b2b",
    #         "framework",
    #     ],
    # )
    # def test_main_page_service_item_block_open_page_card_more(index, name_page, title_page):
    #     with allure.step("Открываем главную страницу"):
    #         page = MainPageSelene()
    #         page.open_page()
    #
    #     with allure.step(f"Открываем страницу '{name_page}' из блока Services"):
    #         page.open_page_from_services_block_by_index(index)
    #
    #     with allure.step("Проверяем URL и заголовок страницы"):
    #         page.check_page_url_and_title(name_page, title_page)
    #
    #
    # @allure.tag("critical")
    # @allure.severity(Severity.CRITICAL)
    # @allure.label("owner", "chernetsova")
    # @allure.story("Открытие страниц блока Project")
    # @allure.link("https://godev.agency/", name="Testing")
    # @pytest.mark.parametrize(
    #     "index, page_name, title_page",
    #     [
    #         (1, "project_euro_vpn", "Information security service redesign"),
    #         (
    #             2,
    #             "project_vegan_hotel",
    #             "Website development for a conceptual hotel in the Dolomites",
    #         ),
    #         (
    #             3,
    #             "project_find_a_builder",
    #             "Website development for London construction company",
    #         ),
    #         (
    #             4,
    #             "project_sls",
    #             "Building a robust logistics platform for Swift Logistic Solutions",
    #         ),
    #         (
    #             5,
    #             "project_mint_link",
    #             "Enhancing Mint Link’s MICE platform for optimal user engagement",
    #         ),
    #     ],
    #     ids=["euro_vpn", "vegan_hotel", "find_a_builder", "sls", "mint_link"],
    # )
    # def test_main_page_project_open_page_card_more(index, page_name, title_page):
    #     with allure.step("Открываем главную страницу"):
    #         page = MainPageSelene()
    #         page.open_page()
    #
    #     with allure.step(f"Открываем страницу '{page_name}' из блока Project"):
    #         page.open_page_from_project_block_by_index(index)
    #
    #     with allure.step("Проверяем URL и заголовок страницы"):
    #         page.check_page_url_and_title(page_name, title_page)



@allure.feature("Отправка заявок")
class TestSendRequests:

    @allure.tag("critical")
    @allure.tag("negative")
    @allure.severity(Severity.CRITICAL)
    @allure.label("owner", "chernetsova")
    @allure.story("Отправка формы из баннера с прикреплением некорректных файлов")
    @allure.title("Отправка формы из баннера с прикреплением некорректных файлов")
    @allure.link("https://godev.agency/", name="Testing")
    @pytest.mark.parametrize(
        "file_name, error_text",
        [
            ("new text.txt", "File `new text.txt` contains potentially malicious code"),
            ("file-txt-5KB.txt", "Invalid file MIME type `file-txt-5KB.txt`"),
            ("testovtt.pfx", "Only PDF, DOCX, TXT, PPT, or PPTX files are allowed"),
            ("25мб.docx", "The file(s) could not be uploaded. File weight exceeded"),
        ],
        ids=["file with regX", "utf-8", "incorrect format file", "large file"],
    )
    def test_main_page_add_incorrect_format_file(self, file_name, error_text):
        with allure.step("Открываем главную страницу"):
            page = MainPageSelene()
            page.open_page()
        with allure.step("Открываем popup из баннера"):
            page.popup_requests.open_popup_in_banner()

        with allure.step("Крепим файл некорректного формата"):
            page.popup_requests.input_comment()
            page.popup_requests.add_file_incorrect_format_in_popup(file_name)

        with allure.step("Жмем на кнопку Get in touch"):
            page.popup_requests.click_button()
        with allure.step("Проверяем сообщение об ошибке при прикреплении некорректного файла"):
            page.popup_requests.get_text_error_file_incorrect_format_in_banner(file_name, error_text)

    # @allure.tag("critical")
    # @allure.tag("negative")
    # @allure.severity(Severity.CRITICAL)
    # @allure.label("owner", "chernetsova")
    # @allure.feature("Негативные кейсы отправки заявок")
    # # @allure.story("Отправка формы из баннера c большим кол-вом файлов")
    # @allure.title("Отправка формы из баннера c большим кол-вом файлов")
    # @allure.link("https://godev.agency/", name="Testing")
    # def test_main_page_add_request_with_add_11_files():
    #     with allure.step("Открываем главную страницу"):
    #         page = MainPageSelene()
    #         page.open_page()
    #     with allure.step("Открываем popup из баннера"):
    #         page.popup_requests.open_popup_in_banner()
    #
    #     with allure.step("Крепим 11 файлов"):
    #         page.popup_requests.input_comment()
    #         page.popup_requests.add_eleven_file_in_popup()
    #
    #     with allure.step("Жмем на кнопку Get in touch"):
    #         page.popup_requests.click_button()
    #     with allure.step("Проверяем сообщение об ошибке при прикреплении кол-ва файлов больше 10"):
    #         page.popup_requests.get_text_error_in_11_files()

    # @allure.tag("critical")
    # @allure.tag("positive")
    # @allure.severity(Severity.CRITICAL)
    # @allure.label("owner", "chernetsova")
    # @allure.feature("Позитивный кейс отправки заявки")
    # # @allure.story("Отправка полностью заполненной формы обратной связи из баннера")
    # @allure.title("Отправка полностью заполненной формы обратной связи из баннера")
    # @allure.link("https://godev.agency/", name="Testing")
    # def test_main_request_in_button_banner():
    #     with allure.step("Открываем главную страницу"):
    #         main_page_test = MainPageSelene()
    #         main_page_test.open_page()
    #     with allure.step("Открываем popup из баннера"):
    #         main_page_test.popup_requests.open_popup_in_banner()
    #     with allure.step("Заполняем форму корректными данными"):
    #         main_page_test.popup_requests.click_topping_random()
    #         main_page_test.popup_requests.input_name()
    #         main_page_test.popup_requests.input_email()
    #         main_page_test.popup_requests.input_phone()
    #         main_page_test.popup_requests.input_comment()
    #     with allure.step("Жмем на кнопку Get in touch"):
    #         main_page_test.popup_requests.click_button()
    #     with allure.step("Проверяем появление окна успешности отправки заявки"):
    #         main_page_test.popup_requests.popup_success_assert()

    #
    #
    # @allure.tag("critical")
    # @allure.tag("negative")
    # @allure.severity(Severity.CRITICAL)
    # @allure.label("owner", "chernetsova")
    # @allure.feature("Негативные кейсы отправки заявок")
    # # @allure.story("Отправка формы из баннера без заполнения полей - поле email")
    # @allure.title("Отправка формы из баннера без заполнения полей - поле email")
    # @allure.link("https://godev.agency/", name="Testing")
    # def test_main_page_empty_field_mail():
    #     with allure.step("Открываем главную страницу"):
    #         main_page_test = MainPageSelene()
    #         main_page_test.open_page()
    #     with allure.step("Открываем popup из баннера"):
    #         main_page_test.popup_requests.open_popup_in_banner()
    #     with allure.step("Жмем на кнопку Get in touch"):
    #         main_page_test.popup_requests.click_button()
    #     with allure.step("Проверяем сообщение об ошибке поля email при полном незаполнении формы"):
    #         main_page_test.popup_requests.get_text_error_in_form_popup()
    #
    #
    # @allure.tag("critical")
    # @allure.tag("negative")
    # @allure.severity(Severity.CRITICAL)
    # @allure.label("owner", "chernetsova")
    # @allure.feature("Негативные кейсы отправки заявок")
    # # @allure.story("Отправка формы из баннера с некорректным заполнением email")
    # @allure.title("Отправка формы из баннера с некорректным заполнением email")
    # @allure.link("https://godev.agency/", name="Testing")
    # @pytest.mark.parametrize(
    #     "email_type",
    #     ["no_at", "no_dot", "cyrillic", "short"],
    #     ids=[
    #         "Email без @",
    #         "Email без .",
    #         "Email с кириллическими символами",
    #         "Короткий Email",
    #     ],
    # )
    # def test_main_page_incorrect_data_email_in_form(email_type):
    #     with allure.step("Открываем главную страницу"):
    #         page = MainPageSelene()
    #         page.open_page()
    #     with allure.step("Открываем popup из баннера"):
    #         page.popup_requests.open_popup_in_banner()
    #     with allure.step("Ввод email"):
    #         page.popup_requests.input_email_in_banner(email_type)
    #     with allure.step("Жмем на кнопку Get in touch"):
    #         page.popup_requests.click_button()
    #     with allure.step("Проверяем сообщение об ошибке для поля email"):
    #         page.popup_requests.get_email_error_message(email_type)
    #
    #
    # @allure.tag("critical")
    # @allure.tag("negative")
    # @allure.severity(Severity.CRITICAL)
    # @allure.label("owner", "chernetsova")
    # @allure.feature("Негативные кейсы отправки заявок")
    # # @allure.story(
    # #     "Отправка формы из баннера с некорректным заполнением поля Имя - с превышением кол-ва символов"
    # # )
    # @allure.title(
    #     "Отправка формы из баннера с некорректным заполнением поля Имя - с превышением кол-ва символов"
    # )
    # @allure.link("https://godev.agency/", name="Testing")
    # def test_main_page_add_request_exceeding_number_of_characters_in_name():
    #     with allure.step("Открываем главную страницу"):
    #         page = MainPageSelene()
    #         page.open_page()
    #
    #     with allure.step("Открываем popup из баннера"):
    #         page.popup_requests.open_popup_in_banner()
    #
    #     with allure.step("Ввод данных в поле Имя с превышением символов"):
    #         page.popup_requests.input_name_in_banner_with_excess()
    #
    #     with allure.step("Жмем на кнопку Get in touch"):
    #         page.popup_requests.click_button()
    #
    #     with allure.step("Проверяем сообщение об ошибке поля email при полном незаполнении формы"):
    #         page.popup_requests.get_text_error_in_form_popup()
    #
    #
    # @allure.tag("critical")
    # @allure.tag("negative")
    # @allure.severity(Severity.CRITICAL)
    # @allure.label("owner", "chernetsova")
    # @allure.feature("Негативные кейсы отправки заявок")
    # # @allure.story(
    # #     "Отправка формы из баннера с некорректным заполнением поля телефон - недостаточное кол-во символов"
    # # )
    # @allure.title(
    #     "Отправка формы из баннера с некорректным заполнением поля телефон - недостаточное кол-во символов"
    # )
    # @allure.link("https://godev.agency/", name="Testing")
    # def test_main_page_add_request_with_incorrect_phone():
    #     with allure.step("Открываем главную страницу"):
    #         page = MainPageSelene()
    #         page.open_page()
    #     with allure.step("Открываем popup из баннера"):
    #         page.popup_requests.open_popup_in_banner()
    #
    #     with allure.step("Ввод 3 символа в поле номера телефона"):
    #         page.popup_requests.input_3_characters_in_field_phone()
    #         page.popup_requests.input_comment()
    #
    #     with allure.step("Жмем на кнопку Get in touch"):
    #         page.popup_requests.click_button()
    #     with allure.step(
    #             "Проверяем сообщение об ошибке при некорректном заполнении поля phone - ввод недостаточного кол-ва символов"
    #     ):
    #         page.popup_requests.get_text_error_in_input_incorrect_phone()


