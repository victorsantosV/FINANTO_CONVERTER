from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import base64
from .get_login import get_login
from .create_bd import create_bd
from .bd import Login

security = HTTPBasic()

def get_tok(username,password):
    log = create_bd(Login.username,Login.password)
    l = get_login(log,username,password)
    if l == False:
        raise HTTPException(401,detail="Login incorreto.")
    user = username.encode('ascii') + password.encode('ascii')
    log = base64.b64encode(user)
    token = log.decode('ascii')
    return token


