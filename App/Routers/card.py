from fastapi import APIRouter, status, HTTPException
from Database.Models.users import Users
from fastapi import HTTPException, status, Depends

from Database.Models.users import Users
from Database.Models.cards import Cards, CardStatusResponseModel
from uuid import UUID
from Helper.oauth2 import get_current_user

router = APIRouter(tags=["Card Status"])


@router.get("/get_card_status", response_model=CardStatusResponseModel)
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
