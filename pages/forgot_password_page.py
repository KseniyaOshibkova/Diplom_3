import allure
from selenium.webdriver.common.by import By

import helpers
from data.url import Url
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input.input__textfield[type='text']")
    RECOVER_BUTTON = (By.XPATH, "//button[contains(@class,'button_button') and text()='Восстановить']")
    HIDE_PASSWORD = (By.XPATH, "//div[contains(@class,'input__icon-action')]")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input.input__textfield[type='text']")


    def __init__(self, driver):
        super().__init__(driver)

    def is_password_field_active(self):
        """Проверка, что поле Пароль подсвечено (содержит класс input_status_active)"""
        with allure.step('Находим родительский div поля'):
            password_div = self.find_element(self.PASSWORD_FIELD).find_element(By.XPATH, "..")
            classes = password_div.get_attribute("class")

        with allure.step('Проверяем, что класс поля Пароль содержит input_status_active'):
            return "input_status_active" in classes


    def go_to_password_recovery_page(self):
        """Метод открывает страницу восстановления пароля через отправку email"""
        with allure.step('Перейти на страницу Входа в аккаунт'):
            self.click_element(self.PERSONAL_ACCOUNT_BUTTON)

        with allure.step('Нажать на кнопку "Восстановить пароль"'):
            self.click_element(self.FORGOT_PASSWORD_BUTTON)

        with allure.step('Проверить переход на страницу восстановление пароля с отправкой email'):
            self.check_current_url(Url.FORGOT_PASSWORD_PAGE)

        with allure.step('Ввести почту'):
            self.fill_input(locator=self.EMAIL_INPUT,
                            value=helpers.random_email())

        with allure.step('Нажать на кнопку "Восстановить"'):
            self.click_element(self.RECOVER_BUTTON)

        with allure.step('Проверить переход на страницу восстановление пароля'):
            self.check_current_url(Url.RESET_PASSWORD)

        with allure.step('Кликнуть по кнопке показать/скрыть пароль'):
            self.click_element(self.HIDE_PASSWORD)

        with allure.step('Проверить, что поле "Пароль" подсвечивается'):
            self.is_password_field_active()


