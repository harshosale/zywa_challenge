from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from Helper.env import envVars
from datetime import datetime, timedelta


TOKEN_EXPIRE_AFTER_MINS = envVars.TOKEN_EXPIRE_AFTER_MINS


class LoginData(BaseModel):
    mobile_number: str


class TokenDataEncoded(BaseModel):
    user_id: str
    exp: datetime = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_AFTER_MINS)


class TokenDataDecoded(BaseModel):
    user_id: Optional[str] = None


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
