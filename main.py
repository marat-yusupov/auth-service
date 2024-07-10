import uuid
from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

class UserAuthData:
    def __init__(self, username, password):
        self.username: str = username
        self.password: str = password

    def __eq__(self, other):
        if isinstance(other, UserAuthData):
            return self.username == other.username and self.password == other.password
        return False

    def __hash__(self):
        return hash((self.username, self.password))

class UserModel:
    def __init__(self, session_id: uuid, account_id: uuid, username: str, account_type: int):
        self.session_id = session_id
        self.account_id = account_id;
        self.username = username
        self.account_type = account_type

mock_account_id = uuid.uuid4();
mock_database = {UserAuthData("vanya.ivanov", "1234567") : UserModel(uuid.uuid4(), mock_account_id, "vanya.ivanov", 0)}

@app.get("/authentification")
async def authentificate(credentials: HTTPBasicCredentials = Depends(security)):
    user_auth_data = UserAuthData(credentials.username, credentials.password)
    user_model = mock_database.get(user_auth_data)

    if user_model is None:
        return {"error": "User no found in database"}
    else:
        return {
            "session_id": user_model.session_id,
            "account_id": user_model.account_id,
            "username": user_model.username,
            "account_type": user_model.account_type
            }