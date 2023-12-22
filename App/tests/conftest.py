import pytest_asyncio
from main import zywa_api
from httpx import AsyncClient
from Database.Models.base_model import BaseModel
from Helper.env import envVars
from Database.create_defaults import create_super_admin, initial_setup


@pytest_asyncio.fixture()
async def client():
    for table in BaseModel.__subclasses__():
        table.create_table()
    initial_setup()
    create_super_admin()

    async with AsyncClient(
        app=zywa_api, base_url="http://localhost:8888"
    ) as testClient:
        yield testClient

    for table in BaseModel.__subclasses__():
        table.drop_table()


@pytest_asyncio.fixture()
async def super_user_token(client):
    user_data = {
        "mobile_number": envVars.SUPER_ADMIN_MOBILE_NUMBER,
    }
    response = await client.post("/login", json=user_data)
    return response.json()["access_token"]
