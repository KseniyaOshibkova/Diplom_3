import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderFeedPage(BasePage):


    ORDER_ITEM_FIRST = (By.XPATH, "(//li[contains(@class,'OrderHistory_listItem__')])[1]/a")
    ORDER_DETAILS_MODAL = (By.XPATH, "//div[contains(@class,'Modal_orderBox__') and "
                                     "contains(@class,'Modal_modal__contentBox__')]")
    FEED_ORDERS_SECTION = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderList__')]")
    FEED_ORDER_ITEMS = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderList__')]/li//p[contains(@class,"
                                  "'text_type_digits-default')]")
    HISTORY_ORDERS_SECTION = (By.XPATH, "//div[contains(@class,'OrderHistory_orderHistory__')]"
                                        "//ul[contains(@class,'OrderHistory_list__')]")
    FIRST_HISTORY_ORDER = (By.XPATH, "//ul[contains(@class,'OrderHistory_profileList')]/li[1]")
    COUNTER_TOTAL = (By.XPATH, "//p[contains(text(),'Выполнено за все время')]/following-sibling::p[contains(@class,"
                               "'OrderFeed_number__')]")
    COUNTER_TODAY = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p[contains(@class,"
                               "'OrderFeed_number__')]")
    IN_PROGRESS_SECTION = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady__') and contains"
                                     "(@class,'OrderFeed_orderList__')]")
    IN_PROGRESS_ORDER_ITEMS = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady__') and "
                                         "contains(@class,'OrderFeed_orderList__')]/li")


    def open_first_order_and_check_modal(self):
        """Метод выполняет следующие действия:
        1. Находит первый заказ в ленте и кликает.
        2. Проверяет, что появилось модальное окно с деталями заказа"""
        with allure.step('Кликнуть по первому заказу в ленте'):
            element = self.waiting_for_element(self.ORDER_ITEM_FIRST)
            element.click()

        with allure.step('Проверить отображение модального окна с деталями заказа'):
            modal = self.waiting_for_element(self.ORDER_DETAILS_MODAL)
            assert modal.is_displayed()


    def should_see_order_in_user_history(self, order_number):
        """Проверяет, что заказ с номером order_number есть в разделе 'История заказов'"""
        with allure.step('Ожидать заказы пользователя'):
            self.waiting_for_element(self.HISTORY_ORDERS_SECTION)
            orders = self.find_elements(self.FIRST_HISTORY_ORDER)

        with allure.step('Проверить наличие заказа в истории заказов пользователя'):
            assert any(order_number == order.text.strip() for order in orders)


    def should_see_order_in_feed(self, order_number):
        """Проверяет, что заказ с номером order_number есть в общей ленте"""
        with allure.step('Ожидать "Ленту заказов"'):
            self.waiting_for_element(self.FEED_ORDERS_SECTION)
            orders = self.find_elements(self.FEED_ORDER_ITEMS)

        with allure.step('Проверить наличие заказа в общем списке заказов'):
            assert any(order_number == order.text.strip() for order in orders)


    def get_total_completed_count(self):
        """Возвращает значение счетчика 'Выполнено за всё время'"""
        element = self.waiting_for_element(self.COUNTER_TOTAL)
        return int(element.text)


    def get_today_completed_count(self):
        """Возвращает значение счетчика 'Выполнено сегодня'"""
        element = self.waiting_for_element(self.COUNTER_TODAY)
        return int(element.text)


    def should_see_new_order_in_progress(self, order_number):
        """Проверяет появление нового заказа в разделе 'В работе'"""
        orders = self.find_elements(self.IN_PROGRESS_ORDER_ITEMS)
        assert any(order_number == order.text.strip() for order in orders)
