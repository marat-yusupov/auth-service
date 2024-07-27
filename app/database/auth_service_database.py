from app.auth import verify_password
from app.database.request_executor import RequestExecutor
from app.models.auth_data import AuthData
from utils.logger import log_error, log_warn


class AuthServiceDatabase:
    def __init__(self):
        self.request_executor = RequestExecutor()

    def get_auth_data(self, username: str, password: str) -> bool:
        query = f"""
SELECT password_hash
FROM auth_data
WHERE username = '{username}'
"""
        hashed_password_as_record = self.request_executor.execute_read_query(query)
        if hashed_password_as_record is None:
            return None
        if len(hashed_password_as_record) == 0:
            log_warn("User not found")
            return None
        if len(hashed_password_as_record) > 1:
            log_error("Found more than one user!")
            return None

        hashed_password_tuple = hashed_password_as_record[0]
        hashed_password = hashed_password_tuple[0]
        if not verify_password(password, hashed_password):
            log_warn("Verification failed")
            return None

        query = f"""
SELECT account_id
FROM auth_data 
WHERE username='{username}'
"""
        auth_data_as_record = self.request_executor.execute_read_query(query)
        if auth_data_as_record is None:
            return None
        if len(auth_data_as_record) == 0 or len(auth_data_as_record) > 1:
            log_error("User not found or found better than one")
            return None
        else:
            return AuthData(auth_data_as_record[0])
