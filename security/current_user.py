from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from jose import JWTError, jwt
from .vars import oauth2_scheme,SECRET_KEY,ALGORITHM
from .authenticate_model import User,TokenData
from .db import login
from .authenticate_user import get_user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(401,detail="O login expirou.",headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(login, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Usuário inativo.")
    return current_user