from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.auth import get_password_hash
from app.database.auth_service_database import AuthServiceDatabase

app = FastAPI()
security = HTTPBasic()


@app.get("/authentification")
def authentification(credentials: HTTPBasicCredentials = Depends(security)):
    hashed_password = get_password_hash(credentials.password)
    print(hashed_password)

    database = AuthServiceDatabase()
    auth_data = database.get_auth_data(credentials.username, hashed_password)
    if auth_data is None:
        return {"error": "User no found in database"}
    else:
        return auth_data.to_json()
