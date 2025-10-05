import allure
from selenium.webdriver.common.by import By

from data.url import Url
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "input.input__textfield[type='text']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input.input__textfield[type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    HIDE_PASSWORD = (By.XPATH, "//div[contains(@class,'input__icon-action')]/svg")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button') and text()='Выход']")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[contains(@class,'Account_link') and text()='История заказов']")


    def __init__(self, driver):
        super().__init__(driver)

    def login_user(self, user_data):
        """Авторизация пользователя с данными из user_data. User_data содержит ключи 'email' и 'password' переданные
         в фикстуре создания пользователя"""
        email = user_data["email"]
        password = user_data["password"]

        with allure.step('Перети по клику на "Личный кабинет"'):
            self.click_element(self.PERSONAL_ACCOUNT_BUTTON)

        with allure.step('Заполнить поля Email и Пароль для авторизации'):
            self.fill_inputs([
                (self.EMAIL_INPUT, email),
                (self.PASSWORD_INPUT, password)])

        with allure.step('Кликнуть по кнопке "Войти"'):
            self.click_element(self.LOGIN_BUTTON)

        with allure.step('Проверить переход на главную страницу'):
             assert self.check_current_url(Url.BASE_URL)


    def go_personal_account(self):
        """Переход в личный кабинет пользователя"""
        with allure.step('Перейти по клику на "Личный кабинет"'):
            self.click_element(self.PERSONAL_ACCOUNT_BUTTON)
            assert self.check_current_url(Url.PROFILE_PAGE)


    def go_to_order_history(self):
        """Переход на страницу Истории заказов"""
        with allure.step('Перейти на страницу Истории заказов'):
            self.click_element(self.ORDER_HISTORY_BUTTON)
            assert self.check_current_url(Url.ORDER_HISTORY_PAGE)


    def logout_personal_account(self):
        """Выход из личного кабинета"""
        with allure.step('Выйти из аккаунта'):
            self.click_element(self.LOGOUT_BUTTON)
            assert self.check_current_url(Url.LOGIN_PAGE)
