import base64
from pydantic import BaseModel

login_list = []

class Login(str):
    username = "finanto"
    password = "Kimetsu-+123"

def login(username,password):
    usr = username.encode('ascii')
    usr = base64.b64encode(usr)
    usuario = usr.decode('ascii')
    pword = password.encode('ascii')
    pword = base64.b64encode(pword)
    senha = pword.decode('ascii')
    login_list.append([usuario,senha])
    return login_list

def get_login(login_list,username,password):
    usr = username.encode('ascii')
    usr = base64.b64encode(usr)
    new_usuario = usr.decode('ascii')
    pword = password.encode('ascii')
    pword = base64.b64encode(pword)
    new_senha = pword.decode('ascii')
    for logli in login_list:
        if new_usuario == logli[0] and new_senha == logli[1]:
            return True
        else:
            return False
            
            
login(Login.username,Login.password)

l = get_login(login_list,"finanto","Kimetsu-+123")
