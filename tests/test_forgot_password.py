import allure


class TestForgotPassword:
    """Тесты на проверку страницы Восстановление пароля"""

    @allure.title("Переход на страницу восстановления пароля")
    @allure.description("Проверить переход на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    def test_go_to_password_recovery_page(self, driver, forgot_password):
        forgot_password.open_recovery_page()

    @allure.title("Отправка email для восстановления")
    @allure.description("Проверить ввод email и нажатие на кнопку 'Восстановить'")
    def test_submit_email_for_recovery(self, driver, forgot_password):
        forgot_password.open_recovery_page()
        forgot_password.submit_email_for_recovery()

    @allure.title("Подсветка поля пароля")
    @allure.description("Проверить, что при клике на кнопку 'показать/скрыть пароль' поле пароля подсвечивается")
    def test_password_field_highlight(self, driver, forgot_password):
        forgot_password.open_recovery_page()
        forgot_password.submit_email_for_recovery()
        forgot_password.toggle_password_visibility_and_check_field()
