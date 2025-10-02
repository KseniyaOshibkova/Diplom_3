import allure

from data.url import Url
from pages.base_page import BasePage


class ConstructorPage(BasePage):



    def __init__(self, driver):
        super().__init__(driver)


    def navigate_(self):
        with allure.step('Переход по клику на "Лента заказов"'):
            self.click_element(self.ORDER_FEED_BUTTON)
            self.check_current_url(Url.ORDER_FEED_PAGE)

        with allure.step('Переход по клику на "Конструктор"'):
            self.click_element(self.CONSTRUCTOR_BUTTON)
            self.check_current_url(Url.BASE_URL)


    def info_about_ingredient_after_click(self):
        with allure.step('Проверить появление окна с деталями об ингредиенте после клика по нему"'):
            self.click_element(self.)
            self.waiting_for_element()

        with allure.step('Закрыть окно'):
            self.click_element(self.)


    def add_ingredient(self):
        with allure.step('Добавление ингредиента в заказ'):


        with allure.step('Проверка изменения каунтера данного ингредиента'):



    def create_order_under_authoriz_user(self):






