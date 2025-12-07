import time

import allure
from selene import browser
from selenium.webdriver.common.by import By


class ScrollElement:

    @allure.step(
        "Прокручиваем страницу к элементу с селектором '{selector}' и индексом '{index}'"
    )
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
    def scroll_to_element(self, selector, index=None, timeout=10, scroll_pause=0.3):
        def is_element_in_viewport(elem):
            # JS проверка, что элемент видим в области просмотра
            js = """
            const el = arguments[0];
            const rect = el.getBoundingClientRect();
            return (
              rect.top >= 0 &&
              rect.left >= 0 &&
              rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
              rect.right <= (window.innerWidth || document.documentElement.clientWidth)
            );
            """
            return browser.driver.execute_script(js, elem)

        # Снимаем фокус с текущего элемента. Без этого костыля - не работает!!!
        browser.element((By.TAG_NAME, "body")).click()

        if index is None:
            element = browser.element(selector)
        else:
            xpath_string = f"({selector})[{index}]"
            element = browser.element((By.XPATH, xpath_string))

        start_time = time.time()
        while True:
            webelement = element.locate()

            if is_element_in_viewport(webelement):
                # Элемент видим — кликаем и выходим из цикла
                webelement.click()
                break

            # Если время ожидания вышло
            if time.time() - start_time > timeout:
                raise TimeoutError(
                    f"Элемент с селектором '{selector}' и индексом '{index}' не стал видимым за {timeout} секунд")

            # Скроллим к элементу (пример плавного скрола центрированно)
            browser.element((By.TAG_NAME, "body")).click() # дополнительный клик (мало ли - не прогрузились js до конца)
            browser.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center', inline: 'center'});", webelement
            )
            time.sleep(scroll_pause)


    @allure.step("Прокручиваем страницу к блоку Other services for you")
    def scroll_element_to_center(self):
        browser.element((By.TAG_NAME, "body")).click()
        element = browser.element(".services-slider-section")
        browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
            element.locate(),
        )
