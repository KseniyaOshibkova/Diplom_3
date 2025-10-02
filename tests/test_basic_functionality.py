import allure


class TestBasicFunc:
    """Тесты на основной функционал заказа"""

    @allure.title("Проверка основного функционала")
    @allure.description("Проверить оформление заказа авторизованным пользователем")
    def test_creating_order_under_authorized_user(self, driver, created_user, personal_account, constructor):
        personal_account.login_user(user_data=created_user)
        constructor.navigate_to_order_feed()
        constructor.navigate_to_constructor()
        constructor.info_about_ingredient_after_click()
        constructor.close_modal_window()
        constructor.drag_ingredient_to_basket()
        constructor.create_order_under_authoriz_user()
