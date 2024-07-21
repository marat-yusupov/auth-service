from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from domain.authentification import Authentification


app = FastAPI()
security = HTTPBasic()


@app.get("/authentification/login")
async def route_login(credentials: HTTPBasicCredentials = Depends(security)):
    return Authentification().try_login(credentials)


@app.get("/authentification/registration")
async def route_register():
    pass
