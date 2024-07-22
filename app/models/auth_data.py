class AuthData:
    account_id: str

    def __init__(self, account_id: str):
        self.account_id = account_id

    def to_json(self) -> dict:
        return {"account_id": self.account_id}
