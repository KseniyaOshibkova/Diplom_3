import allure



class TestOrderFeed:
    """Тесты на проверку раздела Лента заказов"""

    @allure.title("Проверка открытия окна с деталями заказа")
    @allure.description(
        "Проверить, что при клике на заказ в ленте заказов открывается модальное окно с подробной информацией")
    def test_order_details_modal_opens(self, order_feed, constructor):
        constructor.navigate_to_order_feed()
        order_feed.open_first_order_and_check_modal()


    @allure.title("Проверка отображения заказов пользователя в истории и ленте")
    @allure.description("Проверить, что после оформления заказа через UI он должен появляться как в 'Истории заказов',"
                        " так и в общей ленте заказов")
    def test_user_order_appears_in_history_and_feed(self, order_feed, create_new_order, constructor, personal_account):
        order_number = create_new_order

        with allure.step("Проверить, что заказ появился в истории пользователя"):
            personal_account.go_personal_account()
            personal_account.go_to_order_history()
            order_feed.should_see_order_in_user_history(order_number)


        with allure.step("Проверить, что заказ есть в общей ленте заказов"):
            constructor.navigate_to_order_feed()
            order_feed.should_see_order_in_feed(order_number)


    @allure.title("Увеличение счетчиков после создания заказа")
    @allure.description("Проверить, что после оформления нового заказа должны увеличиться счётчики 'Выполнено за всё"
                        " время' и 'Выполнено сегодня'")
    def test_counters_increment_after_order_creation(self, order_feed, create_new_order):
        with allure.step("Получить значения счётчиков до"):
            total_before = order_feed.get_total_completed_count() - 1
            today_before = order_feed.get_today_completed_count() - 1

        with allure.step("Получить значения счётчиков после"):
            total_after = order_feed.get_total_completed_count()
            today_after = order_feed.get_today_completed_count()

        with allure.step("Проверить, что счётчики увеличились на 1"):
            assert total_after == total_before + 1, "Счётчик 'Выполнено за всё время' не увеличился"
            assert today_after == today_before + 1, "Счётчик 'Выполнено сегодня' не увеличился"


    @allure.title("Появление нового заказа в разделе 'В работе'")
    @allure.description("Проверить, что после оформления заказа его номер должен отобразиться в блоке 'В работе'")
    def test_order_appears_in_progress_block(self, order_feed, create_new_order):
        order_number = create_new_order
        order_feed.should_see_new_order_in_progress(order_number)
