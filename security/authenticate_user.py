from security.authenticate_model import UserInDB
from .vars import pwd_context

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(login, username: str):
    if username in login:
        user_dict = login[username]
        return UserInDB(**user_dict)

def authenticate_user(login, username: str, password: str):
    user = get_user(login, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user