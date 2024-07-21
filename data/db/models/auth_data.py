import uuid


class AuthDataModel:
    def __init__(self, session_id: str, account_id: str):
        self.session_id = session_id
        self.account_id = account_id
