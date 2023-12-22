import fastapi
from fastapi import HTTPException, status, Depends

from Database.database import database
from Database.create_defaults import initial_setup, create_super_admin
from Database.Models.users import Users
from Routers import auth
from Database.Models.cards import Cards, CardStatusResponseModel
from uuid import UUID
from Helper.oauth2 import get_current_user

zywa_api = fastapi.FastAPI()


@zywa_api.on_event("startup")
def startup_event():
    if database.is_closed():
        database.connect()
    initial_setup()
    create_super_admin()


@zywa_api.on_event("shutdown")
def shutdown_event():
    if not database.is_closed():
        database.close()


@zywa_api.get("/get_card_status", response_model=CardStatusResponseModel)
def get_card_status(
    card_id: str, mobile_number: str, current_user: UUID = Depends(get_current_user)
):
    users = Users.select().where(
        Users.mobile_number == mobile_number,
    )
    if len(users) == 0:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            "User Account does not exists",
        )
    user = users.get()

    if user.status == 0:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            "Account linked to mobile number has been desabled",
        )
    cards = Cards.select().where(
        Cards.user_id == str(user.id), Cards.card_id == card_id
    )
    if len(cards) == 0:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            "Card for the user does not exists",
        )
    card = cards.dicts().get()

    return card


zywa_api.include_router(auth.router)
