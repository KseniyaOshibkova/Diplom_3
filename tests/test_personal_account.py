import allure


class TestPersonalAccount:
    """Тесты на проверку навигации под авторизованным пользователем"""

    @allure.title("Переход в личный кабинет")
    @allure.description("Проверить, что авторизованный пользователь может перейти в личный кабинет")
    def test_go_to_personal_account(self, driver, created_user, personal_account):
        personal_account.login_user(user_data=created_user)
        personal_account.go_personal_account()

    @allure.title("Переход в раздел История заказов")
    @allure.description("Проверить, что авторизованный пользователь может перейти в раздел История заказов")
    def test_go_to_order_history(self, driver, created_user, personal_account):
        personal_account.login_user(user_data=created_user)
        personal_account.go_personal_account()
        personal_account.go_to_order_history()

    @allure.title("Выход из аккаунта")
    @allure.description("Проверить, что авторизованный пользователь может выйти из аккаунта")
    def test_logout_from_personal_account(self, driver, created_user, personal_account):
        personal_account.login_user(user_data=created_user)
        personal_account.go_personal_account()
        personal_account.logout_personal_account()
