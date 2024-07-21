import uuid
from data.db.auth_service_database import AuthServiceDatabase
from data.db.models.auth_data import AuthDataModel
from data.request.try_login_body import TryLoginBody

mock_account_id = uuid.uuid4()
mock_database = {
    TryLoginBody("vanya.ivanov", "1234567"): AuthDataModel(
        uuid.uuid4(), mock_account_id
    )
}


class Authentification:
    auth_service_database = AuthServiceDatabase()

    def __init__(self):
        pass

    def try_login(self, credentials):
        login_data = TryLoginBody(credentials.username, credentials.password)
        auth_data_dict = self.auth_service_database.get_auth_data(login_data)
        session_id = "c98268b2-222e-40aa-a1fc-8d81d50c2e93"
        account_id = auth_data_dict.get("account_id")
        auth_data_model = AuthDataModel(str(session_id), account_id)

        if auth_data_model is None:
            return {"error": "User no found in database"}
        else:
            return {
                "session_id": auth_data_model.session_id,
                "account_id": auth_data_model.account_id,
            }
