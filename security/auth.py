from fastapi import HTTPException
from fastapi.security import HTTPBasic
from .get_login import get_login
from .create_bd import create_bd
from .bd import Login
import base64

security = HTTPBasic()

def get_tok(username,password):
    log = create_bd(Login.username,Login.password)
    l = get_login(log,username,password)
    if l == False:
        raise HTTPException(401,detail="Usuário ou senha estão incorretos.")
    user = username.encode('ascii') + password.encode('ascii')
    log = base64.b64encode(user)
    token = log.decode('ascii')
    return token


