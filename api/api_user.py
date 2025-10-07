from data.url import Url


class UserApi:
    def __init__(self, client):
        self.client = client

    def create_user(self, user_data):    #добавить данные для создания пользователя
        """Создание пользователя"""
        return self.client.post(Url.CREATE_USER, json=user_data)

    def login_user(self, creds):   #данные для логина
        """Логин пользователя в системе"""
        return self.client.post(Url.LOGIN_USER, json=creds)

    def delete_user(self, access_token):
        headers = {"authorization": f"{access_token}"}
        return self.client.delete(Url.REFRESH_DATA_USERS, headers=headers)
