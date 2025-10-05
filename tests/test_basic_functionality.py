import allure


class TestBasicFunc:
    """Тесты на проверку основного функционала"""

    @allure.title("Оформление заказа авторизованным пользователем")
    @allure.description("Проверить, что авторизованный пользователь может оформить заказ")
    def test_create_order_authorized_user(self, driver, created_user, personal_account, constructor):
        personal_account.login_user(user_data=created_user)
        constructor.drag_ingredient_to_basket()
        constructor.drag_ingredient_meet_to_basket()
        constructor.create_order_under_authoriz_user()

    @allure.title("Переход на страницу конструктора")
    @allure.description("Проверить, что при клике на 'Конструктор' открывается главная страница конструктора")
    def test_navigate_to_constructor(self, driver, constructor):
        constructor.navigate_to_constructor()

    @allure.title("Переход на страницу ленты заказов")
    @allure.description("Проверить, что при клике на 'Лента заказов' открывается страница ленты заказов")
    def test_navigate_to_order_feed(self, driver, constructor):
        constructor.navigate_to_order_feed()

    @allure.title("Открытие окна с деталями ингредиента")
    @allure.description("Проверить, что при клике на ингредиент появляется модальное окно с его деталями")
    def test_open_ingredient_modal(self, driver, constructor):
        constructor.info_about_ingredient_after_click()

    @allure.title("Закрытие окна с деталями ингредиента")
    @allure.description("Проверить, что окно с деталями закрывается при клике на крестик")
    def test_close_ingredient_modal(self, driver, constructor):
        constructor.info_about_ingredient_after_click()
        constructor.close_modal_window()

    @allure.title("Увеличение счётчика ингредиента при добавлении в заказ")
    @allure.description("Проверить, что при добавлении ингредиента в заказ его счётчик увеличивается на 1")
    def test_counter_increment_after_adding_ingredient(self, driver, constructor):
        constructor.drag_ingredient_to_basket()
