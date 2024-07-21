import sqlite3
from sqlite3 import Error

from data.request.try_login_body import TryLoginBody


class AuthServiceDatabase:
    def __init__(self):
        # Путь к базе данных нужно выносить в конфиг.
        # Здесь нужно обращаться к конфигу и брать оттуда путь.
        # В данный момент, это временный вариант.
        self.connection = AuthServiceDatabase.create_connection(
            "/home/myuspv/Pets/database/auth_service.sqlite"
        )

    @staticmethod
    def create_connection(path):
        connection = None

        try:
            connection = sqlite3.connect(path)
            print("Connection to AuthService database successful")
        except Error as error:
            print(f"Error connecting to database. Error: {error}")

        return connection

    def __execute_query(self, connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query executed successfully")
        except Error as error:
            print(f"The error '{error}' occurred")

    def __execute_read_query(self, connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as error:
            print(f"The error '{error}' occurred")

    def get_auth_data(self, login_data: TryLoginBody):
        query = f"SELECT account_id FROM auth_data WHERE username='{login_data.username}' AND password_hash='{login_data.password}'"
        auth_data_record = self.__execute_read_query(self.connection, query)

        if auth_data_record:
            auth_data_dict = dict(zip(["account_id"], auth_data_record))
            return auth_data_dict
        else:
            return None
