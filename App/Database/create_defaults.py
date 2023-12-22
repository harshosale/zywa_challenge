from Database.Models.base_model import BaseModel
from Database.database import database
from Database.Models.users import UserCreateModel, Users
from Database.Models.cards import CardCreateModel, Cards
from datetime import datetime

import os
from csv import DictReader
from enum import Enum


class Csv_Types(Enum):
    DELIVERED = "DELIVERED"
    PICKUP = "PICKUP"
    RETURNED = "RETURNED"
    EXCEPTION = "EXCEPTION"


CSV_COLUMN_MAPPING = {
    Csv_Types.DELIVERED: {
        "ID": "id",
        "Card ID": "card_id",
        "User contact": "user_id",
        "Timestamp": "updated_at",
        "Comment": "comments",
    },
    Csv_Types.PICKUP: {
        "ID": "id",
        "Card ID": "card_id",
        "User Mobile": "user_id",
        "Timestamp": "updated_at",
    },
    Csv_Types.RETURNED: {
        "ID": "id",
        "Card ID": "card_id",
        "User contact": "user_id",
        "Timestamp": "updated_at",
    },
    Csv_Types.EXCEPTION: {
        "ID": "id",
        "Card ID": "card_id",
        "User contact": "user_id",
        "Timestamp": "updated_at",
        "Comment": "comments",
    },
}


def get_date_format(type):
    return {
        Csv_Types.DELIVERED: "%Y-%m-%dT%H:%M:%Sz",
        Csv_Types.PICKUP: "%d-%m-%Y %H:%M %p",
        Csv_Types.RETURNED: "%d-%m-%Y %H:%M%p",
        Csv_Types.EXCEPTION: "%d-%m-%Y %H:%M",
    }[type]


def get_csv_type(i):
    for csv_types in Csv_Types._member_names_:
        if csv_types.lower() in i.lower():
            return Csv_Types(csv_types)
    raise ValueError("Csv type not found")


def initial_setup():
    for table in BaseModel.__subclasses__():
        if not database.table_exists(table.__name__):
            table.create_table()
    base_path = os.getcwd() + "/data"

    for i in os.listdir(base_path):
        csv_type = get_csv_type(i)
        columns = CSV_COLUMN_MAPPING[csv_type]

        with open(base_path + "/" + i, "r") as file:
            data = list(DictReader(file))
            for item in data:
                filtered_item = {}
                for k, v in item.items():
                    filtered_item[columns[k.strip()]] = v.strip().strip('"')
                filtered_item["user_id"] = filtered_item["user_id"][-9:]

                user = Users.select(Users.id).where(
                    Users.mobile_number == filtered_item["user_id"]
                )
                if not user:
                    user = Users.create(
                        **dict(UserCreateModel(mobile_number=filtered_item["user_id"]))
                    )
                filtered_item["user_id"] = str(user.get().id)
                filtered_item["status"] = csv_type.name
                filtered_item["updated_at"] = datetime.strptime(
                    filtered_item["updated_at"], get_date_format(csv_type)
                )

                card = Cards.select(Cards.id, Cards.updated_at).where(
                    Cards.id == filtered_item["id"],
                )
                if not card:
                    card = Cards.create(**dict(CardCreateModel(**filtered_item)))
                if card.get().updated_at < filtered_item["updated_at"]:
                    Cards.update(
                        updated_at=filtered_item["updated_at"],
                        comments=filtered_item.get("comments", card.get().comments),
                        status=filtered_item["status"],
                    ).where(
                        Cards.id == filtered_item["id"],
                    )
