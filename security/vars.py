from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "11d92654622f9780c10cc1669fd8ea4552dc3c94dbae030b0fe47378c8d60012"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")