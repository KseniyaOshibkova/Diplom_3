import random
import string

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.common.exceptions import WebDriverException


def random_email(domain="yandex.ru"):
    """Генерация уникального email"""
    return "test_" + "".join(random.choices(string.ascii_lowercase, k=8)) + f"@{domain}"


class DriverFactory:
    @staticmethod
    def get_driver(browser_name: str):
        """Фабричный метод для создания драйвера браузера.
        :param browser_name: название браузера (chrome или firefox)"""
        browser_name = browser_name.lower()

        if browser_name == "chrome":
            return webdriver.Chrome(service=ChromeService())
        elif browser_name == "firefox":
            return webdriver.Firefox(service=FirefoxService())
        else:
            raise WebDriverException(
                f"Неизвестный браузер: {browser_name}. "
                f"Доступные варианты: chrome, firefox.")
