import base64
from .bd import login_list

def create_bd(username,password):
    usr = username.encode('ascii')
    usr = base64.b64encode(usr)
    usuario = usr.decode('ascii')
    pword = password.encode('ascii')
    pword = base64.b64encode(pword)
    senha = pword.decode('ascii')
    login_list.append([usuario,senha])
    return login_list