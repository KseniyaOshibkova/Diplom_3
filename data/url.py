class Url:
    BASE_URL = "https://stellarburgers.nomoreparties.site/"
    FORGOT_PASSWORD_PAGE = f"{BASE_URL}forgot-password"
    RESET_PASSWORD_PAGE = f"{BASE_URL}reset-password"
    PROFILE_PAGE = f"{BASE_URL}account/profile"
    ORDER_HISTORY_PAGE = f"{BASE_URL}account/order-history"
    LOGIN_PAGE = f"{BASE_URL}login"
    ORDER_FEED_PAGE = f"{BASE_URL}feed"

    CREATE_USER = "/api/auth/register"
    LOGIN_USER = "/api/auth/login"
    REFRESH_DATA_USERS = "/api/auth/user"
