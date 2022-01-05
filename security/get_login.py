import base64

def get_login(log,username,password):
    usr = base64.b64decode(username)
    usr = base64.b64encode(usr)
    new_usr = usr.decode('ascii')
    passw = base64.b64decode(password)
    passw = base64.b64encode(passw)
    new_senha = passw.decode('ascii')
    for logli in log:
        if new_usr == logli[0] and new_senha == logli[1]:
            return True
        else:
            return False