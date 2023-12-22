from fastapi import APIRouter, status, HTTPException
from Database.Models.users import Users
from Database.Models.auths import (
    LoginData,
    LoginResponse,
    TokenDataEncoded,
)
from Helper.oauth2 import create_access_token
from datetime import datetime

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=LoginResponse)
def login(login_data: LoginData):
    users = Users.select().where(Users.mobile_number == login_data.mobile_number)
    if len(users) == 0:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            "User Account does not exists",
        )

    user = users.get()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials"
        )
    if user.access_token is None or (
        user.access_token is not None and user.token_expire_at < datetime.utcnow()
    ):
        user_id = str(user.id)
        token_data = TokenDataEncoded(user_id=user_id)
        token = LoginResponse(access_token=create_access_token(token_data))
        Users.update(
            access_token=token.access_token, token_expire_at=token_data.exp
        ).where(Users.id == user_id, Users.status == 1).execute()
    else:
        token = LoginResponse(access_token=user.access_token)
    return token
