import allure
import pytest

import helpers
from api.api_client import ApiClient
from api.api_user import UserApi
from data.url import Url
from helpers import DriverFactory
from pages.forgot_password_page import ForgotPasswordPage
from pages.personal_account_page import PersonalAccountPage
from pages.order_feed_page import OrderFeedPage
from pages.constructor_page import ConstructorPage


def pytest_addoption(parser):
    """Параметр командной строки --browser"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Браузер для запуска тестов: chrome или firefox")


@pytest.fixture
def driver(request):
    """Фикстура для инициализации и закрытия браузера"""
    browser = request.config.getoption("--browser")
    driver = DriverFactory.get_driver(browser)
    driver.maximize_window()
    driver.get(Url.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def client():
    return ApiClient()


@pytest.fixture
def user_api(client):
    return UserApi(client)


@pytest.fixture(scope='function', autouse=False)
def forgot_password(driver):
    return ForgotPasswordPage(driver)


@pytest.fixture(scope='function', autouse=False)
def constructor(driver):
    return  ConstructorPage(driver)


@pytest.fixture(scope='function', autouse=False)
def order_feed(driver):
    return OrderFeedPage(driver)


@pytest.fixture(scope='function', autouse=False)
def personal_account(driver):
    return PersonalAccountPage(driver)


@pytest.fixture
def created_user(user_api):
    """Создаёт пользователя через API и удаляет его после теста"""
    user_data = {
        "email": helpers.random_email(),
        "password": "Pass1234",
        "name": "TestUser"}
    create_response = user_api.create_user(user_data)
    body = create_response.json()
    token = body.get("accessToken")

    yield user_data  # логин в тесте через UI

    if token:
        user_api.delete_user(token)


@pytest.fixture
def create_new_order(driver, constructor, order_feed, personal_account, created_user):
    """Создает новый заказ через UI и возвращает его номер"""
    with allure.step("Авторизоваться пользователем"):
        personal_account.login_user(user_data=created_user)

    with allure.step("Перейти в конструктор"):
        constructor.navigate_to_constructor()

    with allure.step("Добавить ингредиент Spicy-X в корзину"):
        constructor.drag_ingredient_to_basket()
        constructor.drag_ingredient_meet_to_basket()

    with allure.step("Оформить заказ"):
        constructor.create_order_under_authoriz_user()
        order_number = constructor.get_order_number()

    with allure.step("Закрыть окно с идентификатором заказа"):
        constructor.close_modal_window()

    with allure.step("Перейти в ленту заказов"):
        constructor.navigate_to_order_feed()

        return str(order_number)
