import allure
from selenium.webdriver.common.by import By
from data.url import Url
from pages.base_page import BasePage


class ConstructorPage(BasePage):
    INGREDIENT_SPICY_X = (By.XPATH,
                          "//a[contains(@class,'BurgerIngredient_ingredient') and .//p[text()='Соус Spicy-X']]")
    MODAL_HEADER = (By.XPATH, "//h2[text()='Детали ингредиента']")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")
    INGREDIENT_SPICY_X_COUNTER = (By.XPATH,
        "//a[contains(@class,'BurgerIngredient_ingredient') and .//p[text()='Соус Spicy-X']]//p[contains(@class,"
        "'counter_counter')]")
    BASKET_AREA = (By.XPATH, "//section[contains(@class,'BurgerConstructor_basket')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_MODAL = (By.XPATH, "//p[text()='идентификатор заказа']")


    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_order_feed(self):
        """Метод совершает переход на страницу ленты заказов"""
        with allure.step('Переход по клику на "Лента заказов"'):
            self.click_element(self.ORDER_FEED_BUTTON)
            self.check_current_url(Url.ORDER_FEED_PAGE)

    def navigate_to_constructor(self):
        """Метод совершает переход на страницу конструктора"""
        with allure.step('Переход по клику на "Конструктор"'):
            self.click_element(self.CONSTRUCTOR_BUTTON)
            self.check_current_url(Url.BASE_URL)


    def info_about_ingredient_after_click(self):
        """Метод проверяет появление окна с деталями об ингредиенте"""
        with allure.step('Проверить появление окна с деталями об ингредиенте после клика по нему"'):
            self.click_element(self.INGREDIENT_SPICY_X)
            self.check_displayed_element(self.MODAL_HEADER)


    def close_modal_window(self):
        """Метод закрывает окно с деталями об ингредиенте"""
        with allure.step('Закрыть окно деталей об ингредиенте'):
            self.click_element(self.CLOSE_BUTTON)
            self.check_not_displayed_element(self.MODAL_HEADER)


    def is_counter_incremented_by_one(self, before_value, counter_locator=INGREDIENT_SPICY_X_COUNTER):
        """Метод проверяет, что счётчик увеличился на 1"""
        with allure.step('Получить текущее значение счетчика ингредиента'):
            after_value = int(self.find_element(self.INGREDIENT_SPICY_X_COUNTER).text)
        with allure.step('Проверить, что счётчик увеличился на 1'):
            return after_value == before_value + 1


    def drag_ingredient_to_basket(
            self, ingredient_locator=INGREDIENT_SPICY_X, counter_locator=INGREDIENT_SPICY_X_COUNTER):
        """ Метод перетаскивает ингредиент в область для заказа и проверяет, что счётчик увеличился на 1"""
        with allure.step('Добавление ингредиента в заказ'):
            # Получаем текущее значение счётчика
            before_value = int(self.find_element(counter_locator).text)
            # Находим ингредиент и корзину
            ingredient = self.find_element(ingredient_locator)
            basket = self.find_element(self.BASKET_AREA)
            # Перетаскиваем элемент
            self.drag_and_drop(ingredient, basket)

        with allure.step('Проверяем, что элемент появился в корзине'):
            self.is_element_in_container(self.BASKET_AREA, ingredient_locator)

        with allure.step('Проверяем, что счётчик увеличился на 1'):
            assert self.is_counter_incremented_by_one(before_value, counter_locator)


    def create_order_under_authoriz_user(self):
        """Метод осуществляет клик по кнопке 'Оформить заказ' и проверяет появление идентификатора заказа"""
        with allure.step('Клик по кнопке "Оформить заказ"'):
            self.click_element(self.ORDER_BUTTON)
        with allure.step('Проверка отображения идентификатора заказа'):
            self.check_displayed_element(self.ORDER_MODAL)
