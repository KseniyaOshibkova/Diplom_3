import allure


class TestForgotPassword:
    """Тесты на проверку страницы Восстановление пароля"""

    @allure.title('Восстановление пароля')
    @allure.description('Проверить элементы страницы Восстановление пароля')
    def test_go_to_password_recovery_page_by_clicking_recover_password_button(self, driver, forgot_password):
        forgot_password.go_to_password_recovery_page()
