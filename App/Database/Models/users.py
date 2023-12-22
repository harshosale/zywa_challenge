import peewee
from Database.Models.base_model import BaseModel as dbBaseModel
from pydantic import BaseModel, conint
from uuid import uuid4, UUID
from datetime import datetime
from typing import Optional


class Users(dbBaseModel):
    id = peewee.UUIDField(unique=True, default=uuid4)
    mobile_number = peewee.BigIntegerField(unique=True)
    access_token = peewee.CharField(unique=True, null=True)
    token_expire_at = peewee.DateTimeField(null=True)
    status = peewee.SmallIntegerField(default=1)
    created_at = peewee.DateTimeField(default=datetime.utcnow())
    updated_at = peewee.DateTimeField(default=datetime.utcnow())


class UserCreateModel(BaseModel):
    mobile_number: Optional[conint(gt=99_999_999, lt=1_000_000_000)]


class UserUpdateModel(BaseModel):
    mobile_number: Optional[conint(gt=99_999_999, lt=1_000_000_000)] = None


class UserResponseModel(BaseModel):
    id: UUID
    mobile_number: Optional[int] = None
    access_token: Optional[str] = None
    token_expire_at: Optional[datetime] = None
    status: int
