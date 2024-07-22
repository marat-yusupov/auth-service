from app.database.request_executor import RequestExecutor
from app.models.auth_data import AuthData
from utils.logger import log_error


class AuthServiceDatabase:
    def __init__(self):
        self.request_executor = RequestExecutor()

    def get_auth_data(self, username: str, hashed_password: str) -> AuthData:
        query = """
SELECT account_id 
FROM auth_data 
WHERE username='{username}' AND password_hash='{hashed_password}'
"""
        auth_data_as_record = self.request_executor.execute_read_query(query)
        if auth_data_as_record is None:
            return None
        if len(auth_data_as_record) == 0 or len(auth_data_as_record) > 1:
            log_error("User not found or found better than one")
            return None
        else:
            return AuthData(auth_data_as_record[0])
