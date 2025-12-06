import os
import random
import time
from time import sleep

import allure
from faker.proxy import Faker
from selene import be, browser, have
from selenium.webdriver.common.by import By

from page_elements.cookies_popup import CookiesPopup


class PopupFormRequests:

    def __init__(self):
        self.name_data = Faker()
        self.cookie_modal = CookiesPopup()
        self.constant = "drftv7ybh8im90ok"

    def open_popup(self):
        browser.element((By.TAG_NAME, "body")).click()
        self.cookie_modal.close_modal()
        browser.element(".right .button").click()

    @staticmethod
    # @allure.step("Выбрать случайное количество топпингов")
    def click_topping_random():
        selected_indexes = random.sample(
            range(1, 7), random.randint(1, 6)
        )  # Выбираем индексы топпингов

        for index in selected_indexes:
            element_locator = (
                f"//*[contains(@class, 'sendmail-popup')]//*[@for='t1{index}']"
            )
            browser.element(element_locator).click()
            print(f"Выбран топпинг с индексом: {index}")  # Для отладки

    def open_popup_in_banner(self):
        browser.element((By.TAG_NAME, "body")).click()
        self.cookie_modal.close_modal()
        browser.element(".banner-button").click()

    def input_name(self):
        name_text = self.constant + self.name_data.name()
        browser.element("//*[contains(@class, ' sendmail-popup')]//*[@name='name']").type(
            name_text
        )

    def input_name_in_banner_with_excess(self):
        name_text = self.constant + self.name_data.text(max_nb_chars=350)
        browser.element("//*[contains(@class, ' sendmail-popup')]//*[@name='name']").type(
            name_text
        )

    def input_email(self):
        email_text = self.constant + self.name_data.email()
        browser.element(
            "//*[contains(@class, ' sendmail-popup')]//*[@name='email']"
        ).type(email_text)

    def input_phone(self):
        phone_number = self.name_data.numerify("###########")
        browser.element(
            "//*[contains(@class, ' sendmail-popup')]//*[@name='phone']"
        ).type(phone_number)

    def input_comment(self):
        comment_text = self.constant + self.name_data.text(max_nb_chars=150)
        element = browser.element(
            "//*[contains(@class, ' sendmail-popup')]//*[@name='description']"
        )
        for char in comment_text:
            element.type(char)
            time.sleep(0.05)  # Задержка в 0.1 секунды между вводом символов

    @staticmethod
    def click_button():
        browser.element("//*[contains(@class, ' sendmail-popup')]//button").click()

    @staticmethod
    def popup_success_assert():
        element = browser.element("//*[@class='sendmail-popup success']")
        element.should(be.visible)

    def input_3_characters_in_field_phone(self):
        self.input_email()
        char_phone = random.randint(100, 999)
        browser.element(
            "//*[contains(@class, ' sendmail-popup')]//*[@name='phone']"
        ).type(char_phone)

    @staticmethod
    def get_text_error_in_form_popup():
        error_element = (
            browser.element(
                (By.XPATH, "//*[@class='form-error' and @style= 'display: block;']")
            )
            .with_(timeout=browser.config.timeout * 2)
            .should(be.visible)
        )
        if error_element.matching(have.text("Required field")):
            print("Ошибка появилась корректная")
        else:
            print("Ошибка некорректная!")

    def input_email_in_banner(self, email_type="correct", custom_email=None):
        """
        Ввод email в баннер
        :param email_type: тип email - "correct", "no_at", "no_dot", "cyrillic", "short", "custom"
        :param custom_email: кастомный email для типа "custom"
        """
        email_locator = "//*[contains(@class, ' sendmail-popup')]//*[@name='email']"
        input_field = browser.element(email_locator)

        if custom_email:
            email_text = custom_email
        else:
            if email_type == "no_at":
                email_text = self.constant + self.name_data.text(max_nb_chars=10)
            elif email_type == "no_dot":
                email_text = self.constant + "@" + self.name_data.text(max_nb_chars=10)
            elif email_type == "cyrillic":
                email_text = self.constant + "тестоваяпочта@тест.ру"
            elif email_type == "short":
                email_text = "1@1.com"
            else:
                raise ValueError(f"Неизвестный тип email: {email_type}")
        input_field.type(email_text)
        return email_text

    @staticmethod
    def get_email_error_message(value):
        """
        Проверяет сообщение об ошибке для поля email
        :param value: тип ожидаемой ошибки - "no_at", "no_dot", "cyrillic"
        """
        error_locator = (
            By.XPATH,
            "//*[@class='form-error' and @style= 'display: block;']",
        )
        error_element = (
            browser.element(error_locator)
            .with_(timeout=browser.config.timeout * 2)
            .should(be.visible)
        )

        error_messages = {
            "no_at": "The special @ symbol must be used once",
            "no_dot": "Enter the correct email",
            "cyrillic": "The Cyrillic alphabet cannot be used in the Email field",
            "short": "Enter the correct email",
        }
        expected_message = error_messages.get(value)
        if not expected_message:
            raise ValueError(f"Неизвестный тип ошибки: {value}")

        if error_element.matching(have.text(expected_message)):
            print(f"Ошибка '{expected_message}' появилась корректно")
            return True
        else:
            print(f"Ошибка некорректная! Ожидалось: '{expected_message}'")
            return False

    @staticmethod
    def get_text_error_in_input_incorrect_phone():
        error_element = (
            browser.element(
                (By.XPATH, "//*[@class='form-error' and @style= 'display: block;']")
            )
            .with_(timeout=browser.config.timeout * 2)
            .should(be.visible)
        )
        if error_element.matching(have.text("Enter the correct phone number")):
            print("Ошибка появилась корректная")
        else:
            print("Ошибка некорректная!")

    # @allure.step("Определение пути файла и прикрепление к форме")
    @staticmethod
    def add_file_in_field(file):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        add_file_in_popup_locator = (
            By.XPATH,
            "//*[@class='request-offer-bottom']//input[@type='file']",
        )
        field_file = browser.element(add_file_in_popup_locator).locate()
        # Передача настоящего WebElement
        browser.execute_script("arguments[0].style.display = 'block';", field_file)

        # путь до файла
        file_path = os.path.join(current_dir, "add_files_in_form_request", file)
        # крепим файл
        field_file.send_keys(file_path)

    def add_eleven_file_in_popup(self):
        self.input_email()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        field_file = browser.element(
            (By.XPATH, "//*[@class='request-offer-bottom']//input[@type='file']")
        ).locate()

        # Показываем элемент через JavaScript
        browser.execute_script("arguments[0].style.display = 'block';", field_file)

        # Пути к файлам
        files_dir = os.path.join(current_dir, "add_files_in_form_request")
        file_names = [f"{i}.docx" for i in range(1, 12)]  # 1.docx ... 11.docx
        file_paths = [os.path.join(files_dir, name) for name in file_names]

        # Проверяем существование файлов
        for file_path in file_paths:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Файл {file_path} не существует")
        files_to_attach = "\n".join(file_paths)

        # Прикрепляем все файлы за один вызов
        field_file.send_keys(files_to_attach)

    @allure.step("Крепим 5 файлов")
    def add_5_file_in_popup(self):
        self.input_email()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        field_file = browser.element(
            (By.XPATH, "//*[@class='request-offer-bottom']//input[@type='file']")
        ).locate()

        # Показываем элемент через JavaScript
        browser.execute_script("arguments[0].style.display = 'block';", field_file)

        # Пути к файлам
        files_dir = os.path.join(current_dir, "add_files_in_form_request")
        file_names = [f"document-5mb-{i}1.pdf" for i in range(1, 6)]  # 1.docx ... 11.docx
        file_paths = [os.path.join(files_dir, name) for name in file_names]

        # Проверяем существование файлов
        for file_path in file_paths:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Файл {file_path} не существует")
        files_to_attach = "\n".join(file_paths)

        # Прикрепляем все файлы за один вызов
        field_file.send_keys(files_to_attach)
        sleep(10)

    def add_file_incorrect_format_in_popup(self, value):
        self.input_email()
        self.add_file_in_field(value)

    @staticmethod
    def get_text_error_file_incorrect_format_in_banner(name_value, value):
        if name_value == "new text.txt" or name_value == "file-txt-5KB.txt":
            error_element = (
                browser.element(
                    (
                        By.XPATH,
                        "//*[@class='form-error backend-errors' and @style= 'display: block;']",
                    )
                )
                .with_(timeout=browser.config.timeout * 2)
                .should(be.visible)
            )
        else:
            error_element = (
                browser.element(
                    (By.XPATH, "//*[@class='file-error' and @style= 'display: flex;']")
                )
                .with_(timeout=browser.config.timeout * 2)
                .should(be.visible)
            )
        if error_element.matching(have.text(value)):
            print("Ошибка появилась корректная")
        else:
            print("Ошибка некорректная!")

    @staticmethod
    def get_text_error_in_11_files():
        error_element = (
            browser.element(
                (By.XPATH, "//*[@class='file-error' and @style= 'display: flex;']")
            )
            .with_(timeout=browser.config.timeout * 2)
            .should(be.visible)
        )
        if error_element.matching(
            have.text("Failed to upload files(s). The number of files exceeded")
        ):
            print("Ошибка появилась корректная")
        else:
            print("Ошибка некорректная!")

