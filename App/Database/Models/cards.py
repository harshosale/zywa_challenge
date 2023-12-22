import peewee
from Database.Models.base_model import BaseModel as dbBaseModel
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Cards(dbBaseModel):
    id = peewee.CharField(unique=True)
    card_id = peewee.CharField()
    user_id = peewee.CharField()
    comments = peewee.TextField(null=True)
    status = peewee.CharField()
    created_at = peewee.DateTimeField(default=datetime.utcnow())
    updated_at = peewee.DateTimeField(default=datetime.utcnow())


class CardCreateModel(BaseModel):
    id: str
    card_id: Optional[str] = None
    user_id: Optional[str] = None
    comments: Optional[str] = None
    status: Optional[str] = None
    updated_at: Optional[datetime] = None


class CardUpdateModel(BaseModel):
    id: Optional[str] = None
    card_id: Optional[str] = None
    user_id: Optional[str] = None
    comments: Optional[str] = None
    status: Optional[str] = None
    updated_at: Optional[datetime] = None


class CardResponseModel(BaseModel):
    id: str
    card_id: str
    user_id: str
    comments: str
    status: str


class CardStatusResponseModel(BaseModel):
    comments: Optional[str] = None
    status: str
