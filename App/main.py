import fastapi

from Database.database import database
from Database.create_defaults import initial_setup, create_super_admin
from Routers import auth, card

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


zywa_api.include_router(auth.router)
zywa_api.include_router(card.router)
