import allure
from selene import browser
from selenium.webdriver.common.by import By


class ScrollElement:

    @allure.step(
        "Прокручиваем страницу к элементу с селектором '{selector}' и индексом '{index}'"
    )
    def scroll_to_element(self, selector, index=None):
        # Важно! Снимаем фокус с текущего элемента (например, с поля ввода)
        browser.element((By.TAG_NAME, "body")).click()
        if index is None:
            # Если индекс не указан, просто прокручиваем к блоку
            element = browser.element(selector)
        else:
            # Если индекс указан, прокручиваем к конкретному элементу внутри блока
            xpath_string = f"({selector})[{index}]"  # Создаем XPath с индексом
            element = browser.element((By.XPATH, xpath_string))
        browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element.locate()
        )

    @allure.step("Прокручиваем страницу к блоку Other services for you")
    def scroll_element_to_center(self):
        browser.element((By.TAG_NAME, "body")).click()
        element = browser.element(".services-slider-section")
        browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
            element.locate(),
        )
