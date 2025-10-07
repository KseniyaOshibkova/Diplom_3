import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(@class,'AppHeader_header') and text()='Личный Кабинет']")
    ORDER_FEED_BUTTON =  (By.XPATH, "//a[contains(@class,'AppHeader_header') and .//p[text()='Лента Заказов']]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@class,'AppHeader_header') and .//p[text()='Конструктор']]")

    def __init__(self, driver):
        self.driver = driver

    def waiting_for_element(self, locator):
        """Ожидает заданный элемент"""
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator))
        return element

    def check_current_url(self, url):
        """Проверяет переход на страницу"""
        WebDriverWait(self.driver, 5).until(EC.url_to_be(url))
        return self.driver.current_url == url


    def find_elements(self, locator):
        """Ищет элемент по локатору"""
        by, value = locator
        return self.driver.find_elements(by, value)


    def find_element(self, locator):
        """Ищет элемент по локатору"""
        by, value = locator
        return self.driver.find_element(by, value)


    def click_element(self, locator, timeout=25):
        """Кликает по элементу"""
        element = WebDriverWait(self.driver, timeout).until(
                  EC.element_to_be_clickable(locator))
        element.click()


    def fill_input(self, locator, value):
        """Заполняет поле ввода"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(value)


    def fill_inputs(self, locators_and_values):
        """Заполняет поля ввода переданные в списке"""
        for locator, value in locators_and_values:
            self.fill_input(locator, value)


    def check_displayed_element(self, locator):
        """Проверяет отображение элемента"""
        element = self.waiting_for_element(locator)
        return element.is_displayed()


    def check_not_displayed_element(self, locator):
        """Проверяет, что элемент не отображается"""
        element = WebDriverWait(self.driver, 15).until(
            EC.invisibility_of_element_located(locator))
        return element


    def is_element_in_container(self, container_locator, element_locator, timeout=10):
        """Проверяет, что элемент с заданным локатором отображается внутри указанного контейнера"""
        with allure.step(f'Проверка, что элемент {element_locator} отображается в контейнере {container_locator}'):
            container = self.driver.find_element(*container_locator)
            element = WebDriverWait(container, timeout).until(
                EC.visibility_of_element_located(element_locator))
            return element.is_displayed()


    def drag_and_drop(self, source_element, target_element):
        """Выполняет перетаскивание элемента source в элемент target"""
        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element).perform()


    def scroll_to_element(self, locator):
        """Скроллит страницу до элемента"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)


    def wait_for_text_change(self, locator, old_text, timeout=10):
        """Ждёт, пока текст элемента сменится с old_text на любой другой"""
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.find_element(locator).text.strip() != old_text)
