import base64
from fastapi import HTTPException

def get_login(log,username,password):
    try:
        usr = base64.b64decode(username)
        usr = base64.b64encode(usr)
        new_usr = usr.decode('ascii')
        passw = base64.b64decode(password)
        passw = base64.b64encode(passw)
        new_senha = passw.decode('ascii')
    except BaseException as e:
        print(e)
        raise HTTPException(406,detail=f'Login inválido.')
    for logli in log:
        if new_usr == logli[0] and new_senha == logli[1]:
            return True
        else:
            return False