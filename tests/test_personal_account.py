import allure


class TestPersonalAccount:
    """Тесты на проверку навигации под авторизованным пользователем"""

    @allure.title("Навигация под авторизованным пользователем и выход из аккаунта")
    @allure.description("""
    Проверить, что авторизованный пользователь может:
    1. Перейти в личный кабинет
    2. Перейти на страницу Истории заказов
    3. Выполнить выход из аккаунта
    """)
    def test_navigating_under_authoriz_user_and_logout(self, driver, created_user, personal_account):
        personal_account.login_user(user_data=created_user)
        personal_account.go_personal_account()
        personal_account.go_to_order_history()
        personal_account.logout_personal_account()
