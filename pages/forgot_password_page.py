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
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[.//p[text()='Личный Кабинет']]")
    PASSWORD_FIELD_ACTIVE = (By.CSS_SELECTOR, "div.input.input_status_active")

    def __init__(self, driver):
        super().__init__(driver)

    def open_recovery_page(self):
        """Открывает страницу восстановления пароля по клику на 'Восстановить пароль'"""
        with allure.step("Перейти на страницу 'Личный кабинет'"):
            self.click_element(self.PERSONAL_ACCOUNT_BUTTON)
            assert self.check_current_url(Url.LOGIN_PAGE)

        with allure.step("Нажать на кнопку 'Восстановить пароль'"):
            self.click_element(self.FORGOT_PASSWORD_BUTTON)

        with allure.step("Проверить, что открыта страница восстановления пароля"):
            assert self.check_current_url(Url.FORGOT_PASSWORD_PAGE)


    def submit_email_for_recovery(self, email=None):
        """Вводит email и кликает по кнопке 'Восстановить'"""
        email_value = email or helpers.random_email()
        with allure.step(f"Ввести email: {email_value}"):
            self.fill_input(self.EMAIL_INPUT, email_value)

        with allure.step("Нажать на кнопку 'Восстановить'"):
            self.click_element(self.RECOVER_BUTTON)

        with allure.step("Проверить, что открыта страница сброса пароля"):
            assert self.check_current_url(Url.RESET_PASSWORD_PAGE)


    def toggle_password_visibility_and_check_field(self):
        """Кликает по кнопке 'показать/скрыть пароль' и проверяет, что поле подсвечивается"""
        with allure.step("Кликнуть по кнопке 'показать/скрыть пароль'"):
            self.click_element(self.HIDE_PASSWORD)

        with allure.step("Проверить, что поле пароля подсветилось"):
            assert self.check_displayed_element(self.PASSWORD_FIELD_ACTIVE)
