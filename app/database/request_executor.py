import sqlite3
from sqlite3 import Connection, Error


class RequestExecutor:
    def __init__(self):
        try:
            self.connection = sqlite3.connect(
                "/home/myuspv/Pets/database/auth_service.sqlite"
            )
            print("Connection to AuthService database successful")
        except Error as error:
            self.connection = None
            print(f"Error connecting to database. Error: {error}")

    def execute_query(self, query):
        if self.connection is None:
            print("Connection to database not established")

        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as error:
            print(f"Error execute request to database. Error: {error}")

    def execute_read_query(self, query):
        if self.connection is None:
            print("Connection to database not established")

        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            return cursor.fetchall()
        except Error as error:
            print(f"Error execute request to database. Error: {error}")
            return None
