from jose import JWTError, jwt
from fastapi import Depends, status, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from Helper.env import envVars
from Database.Models.users import Users
from Database.Models.auths import TokenDataEncoded, TokenDataDecoded

SECRET_KEY = envVars.SECRET_KEY
ALGORITHM = envVars.ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data: TokenDataEncoded):
    return jwt.encode(dict(data), SECRET_KEY, algorithm=ALGORITHM)


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
        token_data = TokenDataDecoded(user_id=user_id)
    except JWTError:
        raise credentials_exception
    return token_data


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token = verify_access_token(token, credentials_exception)
    user = Users.select().where(Users.id == token.user_id).get()
    return user
