import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


@pytest.fixture(scope="function", autouse=True)
def driver_setup():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.page_load_strategy = "none"
    chrome_options.add_argument("--start-maximized")

    # Todo - для firefox другие переменные передаются в расширение:
    # chrome_options.add_argument("--width=1920")
    # chrome_options.add_argument("--height=1080")
    driver = webdriver.Chrome(options=chrome_options)

    # Передаем драйвер в Selene
    browser.config.driver = driver

    yield driver
    browser.driver.maximize_window()
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    # attach.add_video(browser)
    browser.quit()
