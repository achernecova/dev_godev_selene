import allure
from allure_commons.types import AttachmentType
from selene import browser, be, by
from selenium.webdriver.common.by import By


class ScrollElement:

    # @allure.step(
    #     "Прокручиваем страницу к элементу с селектором '{selector}' и индексом '{index}'"
    # )
    # def scroll_to_element(self, selector, index=None):
    #     # Важно! Снимаем фокус с текущего элемента (например, с поля ввода)
    #     browser.element((By.TAG_NAME, "body")).click()
    #     if index is None:
    #         # Если индекс не указан, просто прокручиваем к блоку
    #         element = browser.element(selector)
    #     else:
    #         # Если индекс указан, прокручиваем к конкретному элементу внутри блока
    #         xpath_string = f"({selector})[{index}]"  # Создаем XPath с индексом
    #         element = browser.element((By.XPATH, xpath_string))
    #     # browser.execute_script(
    #     #     "arguments[0].scrollIntoView({block: 'center'});", element.locate()
    #     # )
    #     browser.execute_script(
    #         "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
    #         element.locate(),
    #     )
    def scroll_to_element(self, selector, index=None, timeout=10):
        if index is None:
            element = browser.element(selector)
        else:
            xpath_string = f"({selector})[{index}]"
            element = browser.element(by.xpath(xpath_string))

        # Прикрепляем только текстовое описание
        allure.attach(f"Scroll to element: {xpath_string}", attachment_type=AttachmentType.TEXT)

        # Ждём появление элемента
        element.with_(timeout=timeout).should(be.in_dom)

        # Программно пролистываем страницу к элементу
        browser.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
                                      element.locate())

        # # Ждём полное отображение элемента и кликаем
        # element.with_(timeout=timeout).should(be.visible).click()

    @allure.step("Прокручиваем страницу к блоку Other services for you")
    def scroll_element_to_center(self):
        browser.element((By.TAG_NAME, "body")).click()
        element = browser.element(".services-slider-section")
        browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
            element.locate(),
        )

    # Ждём завершения прокрутки
    @staticmethod
    def stop_scroll_condition():
        position = browser.driver.execute_script("return window.scrollY;")
        return position % 1 == 0  # Целочисленность свидетельствует о завершении прокрутки

    def search_element_website_packages(self, selector, value):
        # Получаем элемент
        # element_website_packages = browser.element(f"(//*[@class='team-card']//a)[{value}]")
        element_website_packages = browser.element(f"{selector}[{value}]")
        # Прокручиваем элемент в центр экрана
        browser.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
                                      element_website_packages())
        browser.with_(timeout=5).wait.until(self.stop_scroll_condition)
